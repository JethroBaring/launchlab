<script lang="ts">
	export let data
</script>
<svelte:head>
    <title>
        Assigned Startups
    </title>
</svelte:head>
<div class="h-96">
	<table class="table">
		<thead>
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
					<td>{applicant.name}</td>
					<td>{applicant.group_name}</td>
					<td>{applicant.member_1_name}</td>
					<td>
						<a href={`/mentor/startups/qualified/${applicant.id}`}><button class="btn btn-ghost btn-xs">View</button></a>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
