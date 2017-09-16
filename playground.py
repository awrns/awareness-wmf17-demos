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


sumdata = a.Set(
	a.Stream(
		[
			[1,2],
			[2,3],
			[1,3],
			[8,7],
			[1,2],
			[2,3],
			[1,3],
			[8,7]
		]
	),
	a.Stream(
		[
			[1,2,3],
			[2,3,5],
			[1,3,4],
			[8,7,15],
			[1,2,3],
			[2,3,5],
			[1,3,4],
			[8,7,15]
		]
	)
)


playground = a.LocalOperator(b'localhost')
playground.remote_operators = [
	a.RemoteOperator(b'localhost', port=1601),
	a.RemoteOperator(b'localhost', port=1602)
]


result = playground.search(1, sumdata, 4)

print(result.operations)