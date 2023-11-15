<script lang="ts">
	import { page } from '$app/stores';
	export let data
	console.log($page.data.message)
</script>

<div class="h-96">
	<table class="table">
		<!-- head -->
		<thead class="sticky top-0 bg-slate-50">
			<tr>
				<th>Startup Name</th>
				<th>Group Name</th>
				<th>Leader</th>
				<th class="w-28"></th>
			</tr>
		</thead>
		<tbody>
			{#each data.applicants as applicant}
				<!-- row 1 -->
				<tr class="hover h-20 p-5">
					<td>{applicant.starup_name}</td>
					<td>{applicant.group_name}</td>
					<td>{applicant.member_1_name}</td>
					<td>
						<a href={`/admin/dashboard/applicants/${applicant.id}`}><button class="btn btn-ghost btn-xs">Review</button></a>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
