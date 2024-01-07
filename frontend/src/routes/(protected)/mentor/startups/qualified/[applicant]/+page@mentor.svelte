<script lang="ts">
	import Icon from '$lib/components/icons/icon.svelte';
	import ApplicantProjectDetails from '$lib/components/applicant/ApplicantProjectDetails.svelte';
	import ApplicantGroupInformation from '$lib/components/applicant/ApplicantGroupInformation.svelte';
	import ApplicantReadinessLevel from '$lib/components/applicant/ApplicantReadinessLevel.svelte';
	import { QualifiedReadinessLevel } from '$lib/components/rubrics';
	import QualifiedReadinessLevelUpdate from '$lib/components/rubrics-update/QualifiedReadinessLevelUpdate.svelte';
	export let data;
</script>


<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-5 overflow-scroll h-full">
			<div class="flex gap-5 items-center">
				<a href="/mentor/startups/qualified">
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
					{#if data.scores.length != 0}
					<QualifiedReadinessLevelUpdate questions={data.questions} id={data.info.id} user={'admin'} scores={data.scores} access={data.access}/>
					{:else}
					<QualifiedReadinessLevel questions={data.questions} id={data.info.id} user={"mentor"}/>
					{/if}
					
				</div>
			</div>
		</div>
	</div>
</div>
