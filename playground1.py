import awareness as a


avgdata = a.Set(
	a.Stream(
		[
			[1,2,3,4,5],
			[2,3,4,5,6],
			[1,3,5,7,9],
			[8,7,5,3,2],
			[1,2,3,4,5],
			[2,3,4,5,6],
			[1,3,5,7,9],
			[8,7,5,3,2]
		]
	),
	a.Stream(
		[
			[3],
			[4],
			[5],
			[5],
			[3],
			[4],
			[5],
			[5]
		]
	)
)



playground = a.LocalOperator(b'localhost')
playground.remote_operators = [
	a.RemoteOperator(b'192.168.2.5'),
	a.RemoteOperator(b'192.168.2.6')
]


result = playground.search(1, avgdata, 4)

print(result.operations)