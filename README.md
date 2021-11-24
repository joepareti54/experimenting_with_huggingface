# experimenting_with_huggingface
NMT tests
This is a test on huggingface capabilities for the tv captioning appliance that adds Spanish subtitles to English tv broadcasts. 
The code is from these sites:

hugging face en2es mt https://huggingface.co/Helsinki-NLP/opus-mt-en-es
transformers doc https://huggingface.co/transformers/quicktour.html

and I am using an ubuntu laptop to run the test.

$ python en2es_0.py
skip all the warnings
mi firma favorita es: sólo los paranoicos sobreviven

so it looks great, but unfortunately it does not work on raspberry pi:

running build_rust
      Updating crates.io index
  Traceback (most recent call last):
    File "/home/pi/.local/lib/python3.7/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 363, in <module>
...lots of traceback...
    File "/usr/lib/python3.7/subprocess.py", line 487, in run
      output=stdout, stderr=stderr)
  subprocess.CalledProcessError: Command '['cargo', 'metadata', '--manifest-path', 'Cargo.toml', '--format-version', '1']' died with <Signals.SIGSEGV: 11>.
  ----------------------------------------
  ERROR: Failed building wheel for tokenizers
Failed to build tokenizers
ERROR: Could not build wheels for tokenizers, which is required to install pyproject.toml-based projects

cargo is installed but it seg faults
  
  This is a known issue with the cargo tool, it is a debian bug
