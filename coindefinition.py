Scrypt ={
        	"bdiff1target": 0x0000FFFF00000000000000000000000000000000000000000000000000000000,
        	"module": "ltc_scrypt",
        	"divide_by": 64,
		"ShareTarget": 0x0000ffff00000000000000000000000000000000000000000000000000000000
	}

SHA256 ={
		"bdiff1target": 0x00000000FFFF0000000000000000000000000000000000000000000000000000,
		"module": "hashlib",
		"divide_by": 1,
		"ShareTarget": 0x00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
	}

 
def getSettings(algo):
    if algo.lower() == "scrypt":
       return Scrypt
    elif algo.lower() == "sha256" or algo.lower() == "sha256d" or algo.lower() == "sha":
       return SHA256
