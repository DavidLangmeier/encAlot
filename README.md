# encAlot 1.0

Use **Install.py** to download codecs first.<br>
<br>
**encAlot.py** usage: encAlot.py -enc 'encoder' -sc 'sequence_config' -fn 'filename' -tbr 'targetbitrate1, targetbitrate2, ...' -pre 'vvenc_preset' -thr 'vvenc_threads'<br>
*'encoder'* has to be 'hm', 'vtm' or 'vvenc'<br>
*'sequence_config'* is the sequence specific configuration, has to be at /encAlot/videoSources. There is an example config there.<br>
*'filename'* will be the Prefix of the encoding output filenames, use for better identification of encodings (i.e. short version of source sequence).<br>
*'targetbitrates'* are the desired bitrates for the encodings in bytes per second. Provide 1-n bitrates for 1-n encodings.<br>
*'vvenc_preset'* is only required when using vvenc. Has to be 'faster', 'fast', 'medium', 'slow' or 'slower'.<br>
*'vvenc_threads'* is only required when using vvenc and sets the number of threads for multi-threaded encoding. Default is 1.<br>
<br>
Use **GetMetrics.py** to extract encoding runtime and actual bitrate of all encodings in folder /encAlot/encodingOutput. The scripts also supports extracting VMAF, PSNR and MS-SSIM from xml-files generated with libVMAF. The values are written to a csv-file for further examination.
