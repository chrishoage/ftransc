#!/usr/bin/python
NO_TAGS             = False
SILENT              = False  
VERSION             = open('/usr/share/doc/ftransc/version').read().strip()
LOGFILE             = '/dev/null'
SUPPORTED_FORMATS   = {'mp3', 'wma', 'wav', 'ogg', 'flac', 'm4a', 'mpc', 'wv', 'avi'}
EXTERNAL_FORMATS    = {"mpc", "wv"}
INTERNAL_FORMATS    = SUPPORTED_FORMATS - EXTERNAL_FORMATS
EXTERNAL_ENCODERS   = {
    "mpc"   : "mppenc",
    "wv"    : "wavpack",
    "mp3"   : "lame",
    "ogg"   : "oggenc",
    "m4a"   : "faac",
    "flac"  : "flac",
}
EXTERNAL_ENCODER_OUTPUT_OPT = {
    'mppenc'    : '',
    'lame'      : '',
    'faac'      : '-o',
    'flac'      : '-o',
    'oggenc'    : '-o',
    'wavpack'   : '-o',
}

DEPENDENCIES = {
    'cdparanoia'        : [],
    'ffmpeg'            : list(SUPPORTED_FORMATS),
    }
for audio_format, encoder in EXTERNAL_ENCODERS.iteritems():
    DEPENDENCIES[encoder] = [audio_format]
