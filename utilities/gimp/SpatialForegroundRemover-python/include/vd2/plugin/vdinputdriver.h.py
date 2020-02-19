#	VirtualDub - Video processing and capture application
#	Plugin headers
#	Copyright (C) 1998-2007 Avery Lee, Rights Reserved.
#
#	The plugin headers in the VirtualDub plugin SDK are licensed differently
#	differently than VirtualDub and the Plugin SDK themselves.  This
#	particular file is thus licensed as follows (the "zlib" license):
#
#	This software is provided 'as-is', any express or implied
#	warranty.  In no event will the authors be held liable for any
#	damages arising from the use of self software.
#
#	Permission is granted to anyone to use self software for any purpose,
#	including commercial applications, to alter it and redistribute it
#	freely, to the following restrictions:
#
#	1.	The origin of self software must not be misrepresented; you must
#		not claim that you wrote the original software. If you use self
#		software in a product, acknowledgment in the product
#		documentation would be appreciated but is not required.
#	2.	Altered source versions must be plainly marked as such, must
#		not be misrepresented as being the original software.
#	3.	This notice may not be removed or altered from any source
#		distribution.

#ifndef f_VD2_PLUGIN_VDINPUTDRIVER_H
#define f_VD2_PLUGIN_VDINPUTDRIVER_H

#ifdef _MSC_VER
#pragma once
#pragma pack(push, 8)
#endif

#include "vdplugin.h"

#/ Unsigned 32-bit fraction.
struct VDXFraction
    uint32 mNumerator
    uint32 mDenominator


typedef struct VDXHWNDStruct *VDXHWND
typedef struct VDXBITMAPINFOHEADERStruct
    enum { kCompressionRGB = 0
    uint32			mSize
    sint32			mWidth
    sint32			mHeight
    uint16			mPlanes
    uint16			mBitCount
    uint32			mCompression
    uint32			mSizeImage
    sint32			mXPelsPerMeter
    sint32			mYPelsPerMeter
    uint32			mClrUsed
    uint32			mClrImportant
} VDXBITMAPINFOHEADER

typedef struct VDXWAVEFORMATEXStruct
    enum { kFormatPCM = 1
    uint16			mFormatTag
    uint16			mChannels
    uint32			mSamplesPerSec
    uint32			mAvgBytesPerSec
    uint16			mBlockAlign
    uint16			mBitsPerSample
    uint16			mExtraSize
} VDXWAVEFORMATEX

struct VDXStreamSourceInfo
    VDXFraction		mSampleRate
    sint64			mSampleCount
    VDXFraction		mPixelAspectRatio


# V3+ (1.7.X) only
struct VDXStreamSourceInfoV3
    VDXStreamSourceInfo	mInfo

    enum
        kFlagVariableSizeSamples	= 0x00000001


    uint32			mFlags
    uint32			mfccHandler;	#/< If non-zero, the FOURCC of a codec handler that should be preferred.


class IVDXStreamSource : public IVDXUnknown
public:
    enum { kIID = VDXMAKEFOURCC('X', 's', 't', 's')

    virtual void				VDXAPIENTRY GetStreamSourceInfo(VDXStreamSourceInfo&) = 0

    virtual bool				VDXAPIENTRY Read(sint64 lStart, lCount, *lpBuffer, cbBuffer, *lBytesRead, *lSamplesRead) = 0

    virtual  void *		VDXAPIENTRY GetDirectFormat() = 0
    virtual int					VDXAPIENTRY GetDirectFormatLen() = 0

    enum ErrorMode
        kErrorModeReportAll = 0,
        kErrorModeConceal,
        kErrorModeDecodeAnyway,
        kErrorModeCount


    virtual ErrorMode			VDXAPIENTRY GetDecodeErrorMode() = 0
    virtual void				VDXAPIENTRY SetDecodeErrorMode(ErrorMode mode) = 0
    virtual bool				VDXAPIENTRY IsDecodeErrorModeSupported(ErrorMode mode) = 0

    virtual bool				VDXAPIENTRY IsVBR() = 0
    virtual sint64				VDXAPIENTRY TimeToPositionVBR(sint64 us) = 0
    virtual sint64				VDXAPIENTRY PositionToTimeVBR(sint64 samples) = 0


# V3+ (1.7.X)
class IVDXStreamSourceV3 : public IVDXUnknown
public:
    enum { kIID = VDXMAKEFOURCC('X', 's', 't', '2')

    virtual void				VDXAPIENTRY GetStreamSourceInfoV3(VDXStreamSourceInfoV3&) = 0


class IVDXVideoDecoderModel : public IVDXUnknown
public:
    enum { kIID = VDXMAKEFOURCC('X', 'v', 'd', 'm')

    virtual void				VDXAPIENTRY Reset() = 0
    virtual void				VDXAPIENTRY SetDesiredFrame(sint64 frame_num) = 0
    virtual sint64				VDXAPIENTRY GetNextRequiredSample(bool& is_preroll) = 0
    virtual int					VDXAPIENTRY GetRequiredCount() = 0


class IVDXVideoDecoder : public IVDXUnknown
public:
    enum { kIID = VDXMAKEFOURCC('X', 'v', 'd', 'e')

    virtual  void *		VDXAPIENTRY DecodeFrame( void *inputBuffer, data_len, is_preroll, sampleNumber, targetFrame) = 0
    virtual uint32				VDXAPIENTRY GetDecodePadding() = 0
    virtual void				VDXAPIENTRY Reset() = 0
    virtual	bool				VDXAPIENTRY IsFrameBufferValid() = 0
    virtual  VDXPixmap&	VDXAPIENTRY GetFrameBuffer() = 0
    virtual bool				VDXAPIENTRY SetTargetFormat(int format, useDIBAlignment) = 0
    virtual bool				VDXAPIENTRY SetDecompressedFormat( VDXBITMAPINFOHEADER *pbih) = 0

    virtual bool				VDXAPIENTRY IsDecodable(sint64 sample_num) = 0
    virtual  void *		VDXAPIENTRY GetFrameBufferBase() = 0


enum VDXVideoFrameType
    kVDXVFT_Independent,
    kVDXVFT_Predicted,
    kVDXVFT_Bidirectional,
    kVDXVFT_Null,


struct VDXVideoFrameInfo
    char	mTypeChar
    uint8	mFrameType
    sint64	mBytePosition


struct VDXVideoSourceInfo
    enum DecoderModel
        kDecoderModelCustom,	#/< A custom decoder model is provided.
        kDecoderModelDefaultIP	#/< Use the default I/P decoder model.


    enum Flags
        kFlagNone			= 0,
        kFlagKeyframeOnly	= 0x00000001,
        kFlagAll			= 0xFFFFFFFF


public:
    uint32	mFlags
    uint32	mWidth
    uint32	mHeight
    uint8	mDecoderModel
    uint8	unused[3]


class IVDXVideoSource : public IVDXUnknown
public:
    enum { kIID = VDXMAKEFOURCC('X', 'v', 'd', 's')

    virtual void	VDXAPIENTRY GetVideoSourceInfo(VDXVideoSourceInfo& info) = 0

    virtual bool	VDXAPIENTRY CreateVideoDecoderModel(IVDXVideoDecoderModel **) = 0
    virtual bool	VDXAPIENTRY CreateVideoDecoder(IVDXVideoDecoder **) = 0

    virtual void	VDXAPIENTRY GetSampleInfo(sint64 sample_num, frameInfo) = 0

    virtual bool	VDXAPIENTRY IsKey(sint64 sample_num) = 0

    virtual sint64	VDXAPIENTRY GetFrameNumberForSample(sint64 sample_num) = 0
    virtual sint64	VDXAPIENTRY GetSampleNumberForFrame(sint64 frame_num) = 0
    virtual sint64	VDXAPIENTRY GetRealFrame(sint64 frame_num) = 0

    virtual sint64	VDXAPIENTRY GetSampleBytePosition(sint64 sample_num) = 0


struct VDXAudioSourceInfo
public:
    uint32	mFlags


class IVDXAudioSource : public IVDXUnknown
public:
    enum { kIID = VDXMAKEFOURCC('X', 'a', 'd', 's')

    virtual void VDXAPIENTRY GetAudioSourceInfo(VDXAudioSourceInfo& info) = 0


class IVDXInputOptions : public IVDXUnknown
public:
    enum { kIID = VDXMAKEFOURCC('X', 'i', 'o', 'p')

    virtual uint32		VDXAPIENTRY Write(void *buf, buflen) = 0


class IVDXInputFile : public IVDXUnknown
public:
    enum { kIID = VDXMAKEFOURCC('X', 'i', 'f', 'l')

    virtual bool	VDXAPIENTRY PromptForOptions(VDXHWND, **ppOptions) = 0
    virtual bool	VDXAPIENTRY CreateOptions( void *buf, len, **ppOptions) = 0

    virtual void	VDXAPIENTRY Init( wchar_t *path, *options) = 0
    virtual bool	VDXAPIENTRY Append( wchar_t *path) = 0

    virtual void	VDXAPIENTRY DisplayInfo(VDXHWND hwndParent) = 0

    virtual bool	VDXAPIENTRY GetVideoSource(int index, **ppVS) = 0
    virtual bool	VDXAPIENTRY GetAudioSource(int index, **ppAS) = 0


#######################################/
# IVDXInputFileDriver
#
class IVDXInputFileDriver : public IVDXUnknown
public:
    enum { kIID = VDXMAKEFOURCC('X', 'i', 'f', 'd')

    virtual int		VDXAPIENTRY DetectBySignature( void *pHeader, nHeaderSize, *pFooter, nFooterSize, nFileSize) = 0
    virtual bool	VDXAPIENTRY CreateInputFile(uint32 flags, **ppFile) = 0


struct VDXInputDriverContext
    uint32	mAPIVersion
    IVDPluginCallbacks *mpCallbacks


typedef bool (VDXAPIENTRY *VDXInputDriverCreateProc)( VDXInputDriverContext *pContext, **)

struct VDXInputDriverDefinition
    enum
        kFlagNone				= 0x00000000,
        kFlagSupportsVideo		= 0x00000001,
        kFlagSupportsAudio		= 0x00000002,
        kFlagCustomSignature	= 0x00010000,
        kFlagAll				= 0xFFFFFFFF

    uint32		mSize;				# size of self structure in bytes
    uint32		mFlags
    sint32		mPriority
    uint32		mSignatureLength
     void *mpSignature
     wchar_t *mpFilenameDetectPattern
     wchar_t *mpFilenamePattern
     wchar_t *mpDriverTagName

    VDXInputDriverCreateProc		mpCreate


enum
    # V1 (1.7.4.28204): Initial version
    # V2 (1.7.5): Default I/P frame model fixed.
    kVDXPlugin_InputDriverAPIVersion = 2


#ifdef _MSC_VER
#pragma pack(pop)
#endif

#endif