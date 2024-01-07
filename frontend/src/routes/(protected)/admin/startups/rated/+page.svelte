<script lang="ts">
	export let data
	const x = [1,2,3,4,5,6,7,8,9,10]
</script>
<button class="btn btn-primary" onclick="my_modal_2.showModal()">accept top 10</button>
<dialog id="my_modal_2" class="modal">
	<div class="modal-box w-3/4">
		<table class="table">
			<!-- head -->
			<thead>
				<tr>
					<th>Rank</th>
					<th>Startup Name</th>
					<th>Mentor</th>
				</tr>
			</thead>
			<tbody>
				{#each x as applicant, i}
					<!-- row 1 -->
					<tr class="hover h-16 p-5">
						<td>{i+1}</td>
						<td>{"sample" + applicant}</td>
						<td><select name="" id="">
							<option value="">Jhudiel Munoz</option>
							<option value="">Chris Jerzey Paz</option>
							<option value="">Kyla Manatad</option>
						</select></td>
					</tr>
				{/each}
				<button class="btn btn-primary">approve</button>
			</tbody>
		</table>
	</div>
	<form method="dialog" class="modal-backdrop">
	  <button>close</button>
	</form>
  </dialog>
<div class="h-96">
	<table class="table">
		<!-- head -->
		<thead>
			<tr>
				<th>Startup Name</th>
				<th>Group Name</th>
				<th>Leader</th>
				<th class="w-28"></th>
			</tr>
		</thead>
		<tbody>
			{#each data.applicants as applicant, i}
				<!-- row 1 -->
				<tr class="hover h-20 p-5">
					<td>{applicant.name}</td>
					<td>{applicant.group_name}</td>
					<td>{applicant.member_1_name}</td>
					<td>
						<a href={`/admin/startups/rated/${applicant.id}`}><button class="btn btn-ghost btn-xs">View</button></a>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
