<script lang="ts">
	import Icon from '$lib/components/icons/icon.svelte';
	import ApplicantProjectDetails from '$lib/components/applicant/ApplicantProjectDetails.svelte';
	import ApplicantGroupInformation from '$lib/components/applicant/ApplicantGroupInformation.svelte';
	import ApplicantReadinessLevel from '$lib/components/applicant/ApplicantReadinessLevel.svelte';
	import ApplicantTechnologyCalculator from '$lib/components/applicant/ApplicantTechnologyCalculator.svelte';
	import AssignMentor from '$lib/components/shared/AssignMentor.svelte';
	export let data;
	console.log(data.calculator)
	let selectedMentor = data.mentors[0].id
	const handleMentor = (mentor: number) => {
		selectedMentor = mentor
		console.log(selectedMentor)
	}

</script>


<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-5 overflow-scroll h-full">
			<div class="flex gap-5 items-center">
				<a href="/admin/startups/rated">
					<Icon data1={'M19.5 12h-15m0 0l6.75 6.75M4.5 12l6.75-6.75'} data2={null} />
				</a>
				<h2 class="text-lg text-left">Back</h2>
			</div>
			<div class="flex-1 overflow-scroll">
				<div class="h-0">
					<ApplicantProjectDetails name={data.info.name} capsuleProposal={data.info.capsule_proposal}/>
					<div class="divider" />
					<ApplicantGroupInformation groupName={data.info.group_name} leaderName={data.info.member_1_name} leaderEmail={data.info.member_1_email} leaderNumber={data.info.member_1_number} members={data.info.members} university={data.info.university_name}/>
					<div class="divider" />
					<ApplicantTechnologyCalculator calculator={data.calculator}/>
					<div class="divider" />
					<ApplicantReadinessLevel readiness={data.answers}/>
					<div class="divider"/>
					<AssignMentor mentors={data.mentors} {handleMentor}/>
					
						<div class="flex gap-5 w-full justify-end">
							<form action={`/admin/startups/applicants/${data.params}?/reject`} method="post">
								<button class="btn bg-red-500 hover:bg-red-600 btn-custom text-white normal-case">Reject</button>
							</form>
							<form action={`/admin/startups/rated/${data.info.id}?/approve`} method="post">
								<button class="btn bg-green-500 hover:bg-green-600 btn-custom text-white normal-case">Approve</button>
							</form>
						</div>
				</div>
			</div>
		</div>
	</div>
</div>
