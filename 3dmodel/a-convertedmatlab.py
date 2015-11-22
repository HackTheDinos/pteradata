# Autogenerated with SMOP version
# /usr/local/bin/smop -v CONVERT_meshformat.m CONVERT_voxels_to_stl.m READ_stl.m WRITE_stl.m

from __future__ import division
# try:
#     from runtime import *
# except ImportError:
#     from smop.runtime import *

def CONVERT_meshformat_(*args,**kwargs):
    varargin = cellarray(args)
    nargin = 0-[].count(None)+len(args)

    if nargin == 2 and nargout == 1:
        faces=varargin[1]
        vertex=varargin[2]
        meshXYZ=zeros_(size_(faces,1),3,3)
        for loopa in arange_(1,size_(faces,1)).reshape(-1):
            meshXYZ[loopa,:,1]=vertex[faces[loopa,1],:]
            meshXYZ[loopa,:,2]=vertex[faces[loopa,2],:]
            meshXYZ[loopa,:,3]=vertex[faces[loopa,3],:]
        varargout[1]=[meshXYZ]
    else:
        if nargin == 1 and nargout == 2:
            meshXYZ=varargin[1]
            vertices=matlabarray([[meshXYZ[:,:,1]],[meshXYZ[:,:,2]],[meshXYZ[:,:,3]]])
            vertices=unique_(vertices,char('rows'))
            faces=zeros_(size_(meshXYZ,1),3)
            for loopF in arange_(1,size_(meshXYZ,1)).reshape(-1):
                for loopV in arange_(1,3).reshape(-1):
                    vertref=find_(vertices[:,1] == meshXYZ[loopF,1,loopV])
                    vertref=vertref[vertices[vertref,2] == meshXYZ[loopF,2,loopV]]
                    vertref=vertref[vertices[vertref,3] == meshXYZ[loopF,3,loopV]]
                    faces[loopF,loopV]=vertref
            varargout[1]=[faces]
            varargout[2]=[vertices]
    return varargout
def CONVERT_voxels_to_stl_(STLname=None,gridDATA=None,gridX=None,gridY=None,gridZ=None,*args,**kwargs):
    varargin = cellarray(args)
    nargin = 5-[STLname,gridDATA,gridX,gridY,gridZ].count(None)+len(args)

    if nargin == 6:
        STLformat=lower_(varargin[1])
    else:
        STLformat=char('ascii')
    if size_(gridX,1) > size_(gridX,2):
        gridX=gridX.T
    if size_(gridY,1) > size_(gridY,2):
        gridY=gridY.T
    if size_(gridZ,1) > size_(gridZ,2):
        gridZ=gridZ.T
    if not isequal_(size_(gridDATA),[numel_(gridX),numel_(gridY),numel_(gridZ)]):
        error_(char(' The dimensions of gridDATA do not match the dimensions of gridX, gridY, gridZ.'))
    gridDATA=logical_(gridDATA)
    objectIND=find_(gridDATA == 1)
    objectX,objectY,objectZ=ind2sub_([numel_(gridX),numel_(gridY),numel_(gridZ)],objectIND,nargout=3)
    if objectX[1] != objectX[end()]:
        gridDATA=gridDATA[min_(objectX):max_(objectX),:,:]
        gridX=gridX[min_(objectX):max_(objectX)]
    if objectY[1] != objectY[end()]:
        gridDATA=gridDATA[:,min_(objectY):max_(objectY),:]
        gridY=gridY[min_(objectY):max_(objectY)]
    if objectZ[1] != objectZ[end()]:
        gridDATA=gridDATA[:,:,min_(objectZ):max_(objectZ)]
        gridZ=gridZ[min_(objectZ):max_(objectZ)]
    gridXsteps=gridX[2:end()] - gridX[1:end() - 1]
    gridXlower=gridX - [gridXsteps[1],gridXsteps] / 2
    gridXupper=gridX + [gridXsteps,gridXsteps[end()]] / 2
    gridYsteps=gridY[2:end()] - gridY[1:end() - 1]
    gridYlower=gridY - [gridYsteps[1],gridYsteps] / 2
    gridYupper=gridY + [gridYsteps,gridYsteps[end()]] / 2
    gridZsteps=gridZ[2:end()] - gridZ[1:end() - 1]
    gridZlower=gridZ - [gridZsteps[1],gridZsteps] / 2
    gridZupper=gridZ + [gridZsteps,gridZsteps[end()]] / 2
    voxcountX=numel_(gridX)
    voxcountY=numel_(gridY)
    voxcountZ=numel_(gridZ)
    gridDATAshifted=false_(size_(gridDATA))
    if voxcountX > 2:
        gridDATAwithborder=cat_(1,false_(1,voxcountY,voxcountZ),gridDATA,false_(1,voxcountY,voxcountZ))
        gridDATAshifted=cat_(1,false_(1,voxcountY,voxcountZ),gridDATAshifted,false_(1,voxcountY,voxcountZ))
        gridDATAshifted=gridDATAshifted + circshift_(gridDATAwithborder,[- 1,0,0]) + circshift_(gridDATAwithborder,[1,0,0])
        gridDATAshifted=gridDATAshifted[2:end() - 1,:,:]
    if voxcountY > 2:
        gridDATAwithborder=cat_(2,false_(voxcountX,1,voxcountZ),gridDATA,false_(voxcountX,1,voxcountZ))
        gridDATAshifted=cat_(2,false_(voxcountX,1,voxcountZ),gridDATAshifted,false_(voxcountX,1,voxcountZ))
        gridDATAshifted=gridDATAshifted + circshift_(gridDATAwithborder,[0,- 1,0]) + circshift_(gridDATAwithborder,[0,1,0])
        gridDATAshifted=gridDATAshifted[:,2:end() - 1,:]
    if voxcountZ > 2:
        gridDATAwithborder=cat_(3,false_(voxcountX,voxcountY,1),gridDATA,false_(voxcountX,voxcountY,1))
        gridDATAshifted=cat_(3,false_(voxcountX,voxcountY,1),gridDATAshifted,false_(voxcountX,voxcountY,1))
        gridDATAshifted=gridDATAshifted + circshift_(gridDATAwithborder,[0,0,- 1]) + circshift_(gridDATAwithborder,[0,0,1])
        gridDATAshifted=gridDATAshifted[:,:,2:end() - 1]
    edgevoxelindices=find_(gridDATA == 1 and gridDATAshifted < 6).T
    edgevoxelcount=numel_(edgevoxelindices)
    facetcount=2 * (edgevoxelcount * 6 - sum_(gridDATAshifted[edgevoxelindices]))
    neighbourlist=false_(edgevoxelcount,6)
    meshXYZ=zeros_(facetcount,3,3)
    normalsXYZ=zeros_(facetcount,3)
    facetcountsofar=0
    for loopP in arange_(1,edgevoxelcount).reshape(-1):
        subX,subY,subZ=ind2sub_(size_(gridDATA),edgevoxelindices[loopP],nargout=3)
        if subX == 1:
            neighbourlist[loopP,1]=0
        else:
            neighbourlist[loopP,1]=gridDATA[subX - 1,subY,subZ]
        if subY == 1:
            neighbourlist[loopP,2]=0
        else:
            neighbourlist[loopP,2]=gridDATA[subX,subY - 1,subZ]
        if subZ == voxcountZ:
            neighbourlist[loopP,3]=0
        else:
            neighbourlist[loopP,3]=gridDATA[subX,subY,subZ + 1]
        if subY == voxcountY:
            neighbourlist[loopP,4]=0
        else:
            neighbourlist[loopP,4]=gridDATA[subX,subY + 1,subZ]
        if subZ == 1:
            neighbourlist[loopP,5]=0
        else:
            neighbourlist[loopP,5]=gridDATA[subX,subY,subZ - 1]
        if subX == voxcountX:
            neighbourlist[loopP,6]=0
        else:
            neighbourlist[loopP,6]=gridDATA[subX + 1,subY,subZ]
        facetCOtemp=zeros_(2 * (6 - sum_(neighbourlist[loopP,:])),3,3)
        normalCOtemp=zeros_(2 * (6 - sum_(neighbourlist[loopP,:])),3)
        facetcountthisvoxel=0
        if neighbourlist[loopP,1] == 0:
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXlower[subX],gridYlower[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXlower[subX],gridYlower[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXlower[subX],gridYupper[subY],gridZlower[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[- 1,0,0]
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXlower[subX],gridYupper[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXlower[subX],gridYupper[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXlower[subX],gridYlower[subY],gridZupper[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[- 1,0,0]
            facetcountsofar=facetcountsofar + 2
        if neighbourlist[loopP,2] == 0:
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXlower[subX],gridYlower[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXupper[subX],gridYlower[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXlower[subX],gridYlower[subY],gridZupper[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[0,- 1,0]
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXupper[subX],gridYlower[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXlower[subX],gridYlower[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXupper[subX],gridYlower[subY],gridZlower[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[0,- 1,0]
            facetcountsofar=facetcountsofar + 2
        if neighbourlist[loopP,3] == 0:
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXupper[subX],gridYlower[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXupper[subX],gridYupper[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXlower[subX],gridYlower[subY],gridZupper[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[0,0,1]
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXlower[subX],gridYupper[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXlower[subX],gridYlower[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXupper[subX],gridYupper[subY],gridZupper[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[0,0,1]
            facetcountsofar=facetcountsofar + 2
        if neighbourlist[loopP,4] == 0:
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXupper[subX],gridYupper[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXlower[subX],gridYupper[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXupper[subX],gridYupper[subY],gridZupper[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[0,1,0]
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXlower[subX],gridYupper[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXupper[subX],gridYupper[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXlower[subX],gridYupper[subY],gridZlower[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[0,1,0]
            facetcountsofar=facetcountsofar + 2
        if neighbourlist[loopP,5] == 0:
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXlower[subX],gridYlower[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXlower[subX],gridYupper[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXupper[subX],gridYlower[subY],gridZlower[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[0,- 1,0]
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXupper[subX],gridYupper[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXupper[subX],gridYlower[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXlower[subX],gridYupper[subY],gridZlower[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[0,- 1,0]
            facetcountsofar=facetcountsofar + 2
        if neighbourlist[loopP,6] == 0:
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXupper[subX],gridYupper[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXupper[subX],gridYupper[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXupper[subX],gridYlower[subY],gridZlower[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[1,0,0]
            facetcountthisvoxel=facetcountthisvoxel + 1
            facetCOtemp[facetcountthisvoxel,1:3,1]=[gridXupper[subX],gridYlower[subY],gridZupper[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,2]=[gridXupper[subX],gridYlower[subY],gridZlower[subZ]]
            facetCOtemp[facetcountthisvoxel,1:3,3]=[gridXupper[subX],gridYupper[subY],gridZupper[subZ]]
            normalCOtemp[facetcountthisvoxel,1:3]=[1,0,0]
            facetcountsofar=facetcountsofar + 2
        meshXYZ[facetcountsofar - facetcountthisvoxel + 1:facetcountsofar,:,:]=facetCOtemp
        normalsXYZ[facetcountsofar - facetcountthisvoxel + 1:facetcountsofar,:]=normalCOtemp
    WRITE_stl_(STLname,meshXYZ,normalsXYZ,STLformat)
    if nargout == 2:
        faces,vertices=CONVERT_meshformat_(meshXYZ,nargout=2)
        varargout[1]=[faces]
        varargout[2]=[vertices]
    return varargout
def READ_stl_(stlFILENAME=None,*args,**kwargs):
    varargin = cellarray(args)
    nargin = 1-[stlFILENAME].count(None)+len(args)

    if nargin == 2:
        stlFORMAT=lower_(varargin[1])
    else:
        stlFORMAT=char('auto')
    if strcmp_(stlFORMAT,char('ascii')) == 0 and strcmp_(stlFORMAT,char('binary')) == 0:
        stlFORMAT=IDENTIFY_stl_format_(stlFILENAME)
    if strcmp_(stlFORMAT,char('ascii')):
        coordVERTICES,coordNORMALS,stlNAME=READ_stlascii_(stlFILENAME,nargout=3)
    else:
        if strcmp_(stlFORMAT,char('binary')):
            coordVERTICES,coordNORMALS=READ_stlbinary_(stlFILENAME,nargout=2)
            stlNAME=char('unnamed_object')
    if nargout == 2:
        varargout[1]=[coordNORMALS]
    else:
        if nargout == 3:
            varargout[1]=[coordNORMALS]
            varargout[2]=[stlNAME]
    return coordVERTICES,varargout
def IDENTIFY_stl_format_(stlFILENAME=None,*args,**kwargs):
    varargin = cellarray(args)
    nargin = 1-[stlFILENAME].count(None)+len(args)

    fidIN=fopen_(stlFILENAME)
    fseek_(fidIN,0,1)
    fidSIZE=ftell_(fidIN)
    if rem_(fidSIZE - 84,50) > 0:
        stlFORMAT=char('ascii')
    else:
        fseek_(fidIN,0,- 1)
        firsteighty=char_(fread_(fidIN,80,char('uchar')).T)
        firsteighty=strtrim_(firsteighty)
        firstfive=firsteighty[1:min_(5,length_(firsteighty))]
        if strcmp_(firstfive,char('solid')):
            fseek_(fidIN,- 80,1)
            lasteighty=char_(fread_(fidIN,80,char('uchar')).T)
            if findstr_(lasteighty,char('endsolid')):
                stlFORMAT=char('ascii')
            else:
                stlFORMAT=char('binary')
        else:
            stlFORMAT=char('binary')
    fclose_(fidIN)
    return stlFORMAT
def READ_stlascii_(stlFILENAME=None,*args,**kwargs):
    varargin = cellarray(args)
    nargin = 1-[stlFILENAME].count(None)+len(args)

    fidIN=fopen_(stlFILENAME)
    fidCONTENTcell=textscan_(fidIN,char('%s'),char('delimiter'),char('\\n'))
    fidCONTENT=fidCONTENTcell[:](logical_(not strcmp_(fidCONTENTcell[:],char(''))))
    fclose_(fidIN)
    if nargout == 3:
        line1=char_(fidCONTENT[1])
        if (size_(line1,2) >= 7):
            stlNAME=line1[7:end()]
        else:
            stlNAME=char('unnamed_object')
    if nargout >= 2:
        stringNORMALS=char_(fidCONTENT[logical_(strncmp_(fidCONTENT,char('facet normal'),12))])
        coordNORMALS=str2num_(stringNORMALS[:,13:end()])
    facetTOTAL=sum_(strcmp_(fidCONTENT,char('endfacet')))
    stringVERTICES=char_(fidCONTENT[logical_(strncmp_(fidCONTENT,char('vertex'),6))])
    coordVERTICESall=str2num_(stringVERTICES[:,7:end()])
    cotemp=zeros_(3,facetTOTAL,3)
    cotemp[:]=coordVERTICESall
    coordVERTICES=shiftdim_(cotemp,1)
    return coordVERTICES,coordNORMALS,stlNAME
def READ_stlbinary_(stlFILENAME=None,*args,**kwargs):
    varargin = cellarray(args)
    nargin = 1-[stlFILENAME].count(None)+len(args)

    fidIN=fopen_(stlFILENAME)
    fseek_(fidIN,80,- 1)
    facetcount=fread_(fidIN,1,char('int32'))
    coordNORMALS=zeros_(facetcount,3)
    coordVERTICES=zeros_(facetcount,3,3)
    for loopF in arange_(1,facetcount).reshape(-1):
        tempIN=fread_(fidIN,3 * 4,char('float'))
        coordNORMALS[loopF,1:3]=tempIN[1:3]
        coordVERTICES[loopF,1:3,1]=tempIN[4:6]
        coordVERTICES[loopF,1:3,2]=tempIN[7:9]
        coordVERTICES[loopF,1:3,3]=tempIN[10:12]
        fread_(fidIN,1,char('int16'))
    fclose_(fidIN)
    return coordVERTICES,coordNORMALS
def WRITE_stl_(fileOUT=None,coordVERTICES=None,coordNORMALS=None,*args,**kwargs):
    varargin = cellarray(args)
    nargin = 3-[fileOUT,coordVERTICES,coordNORMALS].count(None)+len(args)

    if nargin == 4:
        STLformat=lower_(varargin[1])
        if strfind_(STLformat,char('binary')):
            WRITE_stlbinary_(fileOUT,coordVERTICES,coordNORMALS)
        else:
            WRITE_stlascii_(fileOUT,coordVERTICES,coordNORMALS)
    else:
        WRITE_stlascii_(fileOUT,coordVERTICES,coordNORMALS)
    return
def WRITE_stlascii_(fileOUT=None,coordVERTICES=None,coordNORMALS=None,*args,**kwargs):
    varargin = cellarray(args)
    nargin = 3-[fileOUT,coordVERTICES,coordNORMALS].count(None)+len(args)

    facetcount=size_(coordNORMALS,1)
    filePREFIX=fileOUT[1:end() - 4]
    outputALL=zeros_(facetcount,3,4)
    outputALL[:,:,1]=coordNORMALS
    outputALL[:,:,2:end()]=coordVERTICES
    outputALL=permute_(outputALL,[2,3,1])
    fidOUT=fopen_([fileOUT],char('w'))
    fprintf_(fidOUT,char('solid %s\\n'),filePREFIX)
    fprintf_(fidOUT,[char('facet normal %e %e %e\\n'),char('  outer loop\\n'),char('    vertex %e %e %e\\n'),char('    vertex %e %e %e\\n'),char('    vertex %e %e %e\\n'),char('  endloop\\n'),char('endfacet\\n')],outputALL)
    fprintf_(fidOUT,char('endsolid %s\\n'),filePREFIX)
    fclose_(fidOUT)
    return
def WRITE_stlbinary_(fileOUT=None,coordVERTICES=None,coordNORMALS=None,*args,**kwargs):
    varargin = cellarray(args)
    nargin = 3-[fileOUT,coordVERTICES,coordNORMALS].count(None)+len(args)

    facetcount=size_(coordNORMALS,1)
    filePREFIX=fileOUT[1:end() - 4]
    outputALL=zeros_(facetcount,3,4)
    outputALL[:,:,1]=coordNORMALS
    outputALL[:,:,2:end()]=coordVERTICES
    outputALL=permute_(outputALL,[2,3,1])
    fidOUT=fopen_([fileOUT],char('w'))
    headerdata=int8_(zeros_(80,1))
    bytecount=fwrite_(fidOUT,headerdata,char('int8'))
    facetcount=int32_(size_(coordNORMALS,1))
    bytecount=fwrite_(fidOUT,facetcount,char('int32'))
    for loopB in arange_(1,facetcount).reshape(-1):
        fwrite_(fidOUT,outputALL[loopB * 12 - 11:loopB * 12],char('float'))
        fwrite_(fidOUT,0,char('int16'))
    fclose_(fidOUT)
    return

import time
import sys
import glob
import numpy as np
import matplotlib.pyplot as plt
import skimage as sk
from PIL import Image
from mpl_toolkits.mplot3d import axes3d
%pylab inline

# # path for image corpus
# pathCoronal = '../../Zanabazar/CORONAL/*.*';
# pathSagittal = '../../Zanabazar/SAGITTAL/*.*';
# pathHorizon = '../../Zanabazar/HORIZON/*.*';
# directionForward = True;
# path = pathCoronal;

# # variables
# X = []
# Y = []
# Z = []
# image3D = [];                 # container for 3D image data
# maxSize = None;
transparencyThreshold = 155;  # threshold for setting transparent values

# images = glob.glob(path);     # get all images in the folder
# if not directionForward:
#     print "Iterating backwards";
#     images.reverse();

# # iterate through all images in folder
# for index, image in enumerate(images):
#     print 'Processing image #' + str(index) + ": " + image;
#     Z.append(index);
#     img = Image.open(image);   # open the image
#     img = img.convert("RGBA"); # convert image to RGBA format
# #     pixels = img.getdata();    # get pixel data
#     pixels = np.asarray(img);

#     if not maxSize:
#         maxSize = pixels.shape;
#         print maxSize;

#     # iterate through all pixel data
#     newPixels = [];
#     rgb = None;
#     for x in xrange(0, maxSize[0]):
#         for y in xrange(0, maxSize[1]):
#             rgb = pixels[x][y];
# #             print x, y, rgb;
#             X.append(x);
#             Y.append(y);
#             mean = (rgb[0] + rgb[1] + rgb[2]) / 3;
#             # if pixel value less than threshold
#             if mean <= transparencyThreshold:
#                 newPixels.append(0);  # make 0 for exclude in object
#             else: # otherwise make it 1 for include in object
#                 newPixels.append(1);
#     image3D.append(newPixels);


# print image3D.shape;
# import itertools

print "loading numpy array";
image3D = np.load('zbar_cor.npy');
print image3D.shape;
X = range(0, len(image3D))
Y = range(0, len(image3D[0]))
Z = range(0, len(image3D[0][0]))
numImages = len(Z);
print len(X), len(Y), numImages;

for (x,y,z), value in np.ndenumerate(image3D):
    if z % numImages == 0:
        print x, y, z;
    if value > transparencyThreshold:
        image3D[x][y][z] = 1;
    else:
        image3D[x][y][z] = 0;
print "finished thresholding"

print np.max(image3D);

CONVERT_voxels_to_stl_('temp.stl', image3D, X, Y, Z, 'ascii');
print "finished converting voxels"

