import awareness as a



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


playground = a.LocalOperator(b'localhost', port=1601)
playground.remote_operators = [
	a.RemoteOperator(b'192.168.2.5'),
	a.RemoteOperator(b'192.168.2.6')
]


result = playground.search(1, sumdata, 4)

print(result.operations)