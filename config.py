### Settings relating to server identity

# Choose between SHA256, Scrypt, ScryptN, X11
Algorithm = 'Scrypt'

Coin = 'LTC'

# Automatically adjust targets per username 0 = disabled 1 = arbitrary targets 2 = power of two difficulties (zero bit counts)
DynamicTargetting = 3

# How many shares per minute to try to achieve on average
DynamicTargetGoal = 8

# Number of seconds hashrate is measured over
DynamicTargetWindow = 300

# How long to wait between getmemorypool updates normally
MinimumTxnUpdateWait = 5

# How long to wait between retries if getmemorypool fails
TxnUpdateRetryWait = 1

# How long to sleep in idle loops (temporary!)
IdleSleepTime = 0.1

# JSON-RPC server for getmemorypool
UpstreamURI = 'http://username:password@localhost:8002'

# Secret username allowed to use setworkaux
SecretUser = "ssecreteloipool"

# URI to send gotwork with info for every share submission
GotWorkURI = 'http://mergedproxyuser:mergedproxypass@127.0.0.1:8331/'

StratumAddresses = (
	('', 3334),
)

# Logging of shares:
ShareLogging = (
	{
		'type': 'sql',
		'engine': 'mysql',
		'dbopts': {
			'host': 'localhost',
			'db': 'multicoin',
			'user': 'root',
		},
		'statement': "insert into shares (user, ip, oresult, uresult, reason, solution, difficulty, time, coin, blkheight) values ({username}, {remoteHost}, {ourResult}, {upstreamResult}, {reason}, unhex({solution}), {difficulty}, {time}, {coin}, {blkheight})",
	},
)

# Authentication
# There currently are 2 modules.
# - allowall will allow every username/password combination
# - simplefile will use the username/passwords from a file, which contains username<tab>password\n with no \n on the last line.
Authentication = (
	{
		'module': 'allowall',
	},
)

