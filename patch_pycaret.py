"""
Automatic PyCaret Python 3.12 Compatibility Patcher
This script patches PyCaret to work with Python 3.12
"""
import sys
import os

def patch_pycaret():
    """Patch PyCaret to work with Python 3.12"""
    try:
        # Find PyCaret installation
        import pycaret
        pycaret_init_path = pycaret.__file__
        
        # Read the file
        with open(pycaret_init_path, 'r') as f:
            content = f.read()
        
        # Check if already patched
        if 'elif False: # sys.version_info >= (3, 12):' in content:
            print("✓ PyCaret already patched for Python 3.12")
            return True
        
        # Check if patch is needed
        if 'elif sys.version_info >= (3, 12):' not in content:
            print("✓ PyCaret doesn't need patching")
            return True
        
        # Apply patch
        patched_content = content.replace(
            'elif sys.version_info >= (3, 12):',
            'elif False: # sys.version_info >= (3, 12):'
        )
        
        # Try to write the patch
        try:
            with open(pycaret_init_path, 'w') as f:
                f.write(patched_content)
            print("✓ Successfully patched PyCaret for Python 3.12")
            return True
        except PermissionError:
            print("\n" + "="*60)
            print("⚠️  MANUAL PATCH REQUIRED")
            print("="*60)
            print(f"\nPyCaret needs to be patched for Python 3.12.")
            print(f"\nPlease run this command with appropriate permissions:")
            print(f"\n  python patch_pycaret.py --force")
            print(f"\nOr manually edit this file:")
            print(f"  {pycaret_init_path}")
            print(f"\nChange line 21 from:")
            print(f"  elif sys.version_info >= (3, 12):")
            print(f"To:")
            print(f"  elif False: # sys.version_info >= (3, 12):")
            print("\n" + "="*60 + "\n")
            return False
            
    except ImportError:
        print("⚠️  PyCaret not installed. Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Error patching PyCaret: {e}")
        return False

if __name__ == "__main__":
    if "--force" in sys.argv:
        # Try with elevated permissions if available
        import pycaret
        pycaret_init_path = pycaret.__file__
        
        with open(pycaret_init_path, 'r') as f:
            content = f.read()
        
        patched_content = content.replace(
            'elif sys.version_info >= (3, 12):',
            'elif False: # sys.version_info >= (3, 12):'
        )
        
        with open(pycaret_init_path, 'w') as f:
            f.write(patched_content)
        print("✓ PyCaret patched successfully!")
    else:
        patch_pycaret()
