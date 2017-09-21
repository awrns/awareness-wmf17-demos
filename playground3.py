import awareness as a


sumdata2 = a.Set(
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
			[3, 8],
			[5, 10],
			[4, 14],
			[15, 7],
			[3, 8],
			[5, 10],
			[4, 14],
			[15, 7]
		]
	)
)


playground = a.LocalOperator(b'localhost')
playground.remote_operators = [
	a.RemoteOperator(b'localhost', port=1601),
	a.RemoteOperator(b'localhost', port=1602)
]


result = playground.search(1, sumdata2, 4)

print(result.operations)