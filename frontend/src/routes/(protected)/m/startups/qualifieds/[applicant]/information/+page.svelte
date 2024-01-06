<script lang="ts">
	import ApplicantGroupInformation from '$lib/components/applicant/ApplicantGroupInformation.svelte';
	import ApplicantProjectDetails from '$lib/components/applicant/ApplicantProjectDetails.svelte';
	import ApplicantReadinessLevel from '$lib/components/applicant/ApplicantReadinessLevel.svelte';

    export let data;
</script>

<ApplicantProjectDetails name={data.info.name} capsuleProposal={data.info.capsule_proposal} />
<div class="divider" />
<ApplicantGroupInformation
	groupName={data.info.group_name}
	leaderName={data.info.member_1_name}
	leaderEmail={data.info.member_1_email}
	leaderNumber={data.info.member_1_number}
	members={data.info.members}
	university={data.info.university_name}
/>
<div class="divider" />
<ApplicantReadinessLevel readiness={data.readiness} />
