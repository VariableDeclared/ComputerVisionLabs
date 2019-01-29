

# Software
    PixelAnnotationTool

# Dataset
    xview_datasetd

# Methods
- Canny seems good for highlighting routes...!
    - IM AN IDIOT, XDATAVIEW CAME WITH TRAINING DOC

# Issues encountered
- Opening Geojson file (1 day lost)
- Breaking issues down into multiple issues (1 day lost)
- Memmory issues when trying out Mask-RCNN algos. 

# Deployment Issues - Windows
- Tensorflow pip package issues deployment with Cuda
  - More [here](https://github.com/protocolbuffers/protobuf/issues/5046#issuecomment-413726611) and [here](https://github.com/protocolbuffers/protobuf/issues/5046#issuecomment-413726611)

## Tensorflow windows deployment
### Issues:
**Notes**

**Tensorflow**
There was issues downloading initially... due to tensorflow not supporting python version I was using, (Python 3.7)
Moving to lower version of python (3.6), I can now download tensorflow.
Used older version to be sure of working state (version used in blog posts, as starting point v1.6.0). This worked, although required some tinkering with cuda installation.
Installing newer version now.
**Issue with DLL loading in tensorflow 1.12.0**
Issue is to do with protobuf 3.6.1, downgrading to 3.6.0 fixes the issue.
**Issues compiling TF for linux**
- Bazel
- Numpy installation in python3.7
- Python 3.7 having reserved *async* keyword and it being used by the source
- CUDA issues, having to switch to tf-nightly (master) build in order to build tensorflow

**Potential issues upcoing**
- Cuda installation keeps giving compiler warnings, possible upgrade of CUDA could break installation

**Scikit anti-aliasing warning**
pip uninstall scikit-image
pip install scikit-image==0.13.0


**VIRTUALENV SETUP - WINDOWS**
```
pip install .\Shapely-1.6.4.post1-cp36-cp36m-win_amd64.whl
pip install -r .\Mask_RCNN\requirements.txt
pip uninstall tensorflow
pip install tf-nightly tf-nightly-gpu
```