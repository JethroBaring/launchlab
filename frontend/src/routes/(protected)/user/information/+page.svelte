<script lang="ts">
	import ApplicantGroupInformation from '$lib/components/applicant/ApplicantGroupInformation.svelte';
	import ApplicantMentor from '$lib/components/applicant/ApplicantMentor.svelte';
	import ApplicantProjectDetails from '$lib/components/applicant/ApplicantProjectDetails.svelte';
	import Icon from '$lib/components/icons/icon.svelte';

	export let data;
	console.log(data.info);
</script>

<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-5 overflow-scroll h-full w-full mx-auto">
			<h2 class="text-2xl font-bold text-left">Information</h2>
			<div class="flex-1 overflow-scroll flex flex-col gap-5">
				<div class="flex flex-1 flex-col">
					<div class="flex flex-col flex-1 gap-10">
						<div class="flex flex-col gap-5 overflow-scroll h-full">
							<div class="flex-1 overflow-scroll">
								<div class="h-0">
									<ApplicantProjectDetails
										name={data.info.name}
										capsuleProposal={data.info.capsule_proposal}
									/>
									<div class="divider" />
                                    <ApplicantMentor mentor={data.mentor[0]}/>
									<div class="divider" />
									<ApplicantGroupInformation
										groupName={data.info.group_name}
										leaderName={data.info.member_1_name}
										leaderEmail={data.info.member_1_email}
										leaderNumber={data.info.member_1_number}
										members={data.info.members}
										university={data.info.university_name}
									/>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
