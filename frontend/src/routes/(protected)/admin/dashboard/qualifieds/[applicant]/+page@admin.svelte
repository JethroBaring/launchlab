<script lang="ts">
    export let data;
</script>
<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-3 overflow-scroll h-full">
			<div class="flex gap-5 items-center">
                <a href="/admin/dashboard/qualifieds"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                  </svg>
                  </a>
                <h2 class="text-xl font-bold text-left">{data.info.starup_name}</h2>
            </div>
			<div class="flex-1 overflow-scroll">
                <h1>{data.info.starup_name}'s information</h1>
                <h2>Group Name: {data.info.group_name}</h2>
                <p>Leader: {data.info.member_1_name}</p>
                <div>
                    <p>Members</p>
                    <p>{data.info.member_2_name}</p>
                    <p>{data.info.member_3_name}</p>
                    <p>{data.info.member_4_name}</p>
                    <p>{data.info.member_5_name}</p>
                </div>
            </div>
		</div>
	</div>
</div>
