import wave,sys,struct,json,math
if len(sys.argv)<2: raise SystemExit('Usage: python main.py audio.wav')
with wave.open(sys.argv[1],'rb') as w:
 if w.getsampwidth()!=2: raise SystemExit('Use 16-bit PCM WAV')
 v=struct.unpack('<%dh'%(w.getnframes()*w.getnchannels()),w.readframes(w.getnframes())); rms=(sum(x*x for x in v)/max(1,len(v)))**.5
 print(json.dumps({'peak':max(map(abs,v)),'rms':round(rms,1),'rms_dbfs':round(20*math.log10(max(rms,1)/32768),2)},indent=2))