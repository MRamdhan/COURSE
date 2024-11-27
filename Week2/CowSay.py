import cowsay
import sys

message = " ".join(sys.argv[1:])
cowsay.trex(f"Hello {message}")