# Secret username allowed to use setworkaux
SecretUser = "ssecreteloipool"

# URI to send gotwork with info for every share submission
GotWorkURI = 'http://mergedproxyuser:mergedproxypass@127.0.0.1:8331/'

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

# Dynamically Configured Settings

