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

fresh ={
		"bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000
		"module": "fresh_hash",
		"divide_by":1,
		"ShareTarget": 0x00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
	}

mgroestl = {
		"bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000
		"module": "groestl_hash",
		"divide_by": 1,
		"ShareTarget": 0x00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
	}
quark = {
                "bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000
                "module": "quark_hash",
                "divide_by": 1,
                "ShareTarget": 0x00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        }

groestl = {
                "bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000,
                "module": "groestlcoin_hash",
                "divide_by": 1,
                "ShareTarget": 0x00000000ffff0000000000000000000000000000000000000000000000000000
        }

nist5 ={
                "bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000,
                "module": "nist5_hash",
                "divide_by": 1,
                "ShareTarget":0x00000000ffff0000000000000000000000000000000000000000000000000000
        }

scrypt-n = {
                "bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000,
                "module": "vtc_scrypt"
                "divide_by": 1,
                "ShareTarget": 0x00000000ffff0000000000000000000000000000000000000000000000000000 
        }

x11 = {
                "bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000,
                "module": "xcoin_hash",
                "divide_by": 1,
                "ShareTarget": 0x00000000ffff0000000000000000000000000000000000000000000000000000
        }

x13 = {
                "bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000,
                "module": "x13_hash",
                "divide_by": 1,
                "ShareTarget": 0x00000000ffff0000000000000000000000000000000000000000000000000000
        }

x14 = {
                "bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000,
                "module": "x14_hash",
                "divide_by": 1,
                "ShareTarget": 0x00000000ffff0000000000000000000000000000000000000000000000000000
        }

x15 = {
                "bdiff1target": 0x00000000ffff0000000000000000000000000000000000000000000000000000,
                "module": "x15_hash",
                "divide_by": 1,
                "ShareTarget": 0x00000000ffff0000000000000000000000000000000000000000000000000000
        }

 
def getSettings(algo):
    if algo.lower() == "scrypt":
	return Scrypt
    elif algo.lower() == "sha256" or algo.lower() == "sha256d" or algo.lower() == "sha":
	return SHA256
    elif algo.lower() == "fresh":
	return fresh
    elif algo.lower() == "mgroestl":
	return mgroestl
    elif algo.lower() == "quark":
	return quark
    elif algo.lower() == "groestl":
	return groestl
    elif algo.lower() == "nist5"
	return nist5
    elif algo.lower() == "scrypt-n"
	return scrypt-n
    elif algo.lower() == "x11"
	return x11
    elif algo.lower() == "x13"
	return x13
    elif algo.lower() == "x14"
	return x14
    elif algo.lower() == "x15"
	return x15

