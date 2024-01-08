<script lang="ts">
	export let data;
	console.log()
</script>

<div class="flex w-full justify-end">
	<button class="btn btn-primary normal-case btn-custom" onclick="my_modal_2.showModal()"
		>Approve Top 10</button
	>
</div>
<dialog id="my_modal_2" class="modal w-full">
	<div class="modal-box w-3/4">
		<form action="/admin/startups/rated?/approveTopTen" method="post">
			<table class="table">
				<!-- head -->
				<thead>
					<tr>
						<th class="w-28">Rank</th>
						<th>Startup Name</th>
						<th>Mentor</th>
					</tr>
				</thead>
				<tbody>
					{#each data.applicants.filter((applicant) => applicant.qualification_status === 2).slice(0, 10) as applicant, i}
						<tr class="hover h-16">
							<input type="hidden" name={`startup${i + 1}Id`} value={applicant.id} />
							<td>{i + 1}</td>
							<td>{applicant.name}</td>
							<td>
								<select name={`startup${i + 1}Mentor`} class="select">
									{#each data.mentors as mentor}
										<option value={mentor.id}>{mentor.first_name} {mentor.last_name}</option>
									{/each}
								</select>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
			<div class="flex w-full justify-end mt-5">
				<button class="btn btn-primary btn-custom" type="submit">Approve</button>
			</div>
		</form>
	</div>
	<form method="dialog" class="modal-backdrop">
		<button>close</button>
	</form>
</dialog>

<div class="h-96">
	<table class="table">
		<thead>
			<tr>
				<th>Rank</th>
				<th>Startup Name</th>
				<th>Group Name</th>
				<th>Leader</th>
				<th class="w-28" />
			</tr>
		</thead>
		<tbody>
			{#each data.applicants.filter((applicant) => applicant.qualification_status === 2) as applicant, i}
				<tr class="hover h-20 p-5">
					<td>{i + 1}</td>
					<td>{applicant.name}</td>
					<td>{applicant.group_name}</td>
					<td>{applicant.member_1_name}</td>
					<td>
						<a href={`/admin/startups/rated/${applicant.id}`}
							><button class="btn btn-ghost btn-xs">View</button></a
						>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
