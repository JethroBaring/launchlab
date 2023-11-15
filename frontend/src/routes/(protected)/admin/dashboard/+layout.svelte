<script lang="ts">
	import { message } from "../../../../stores/message";
	let applicant = true;
	const handleClick = () => {
		applicant = !applicant;
	};
</script>

<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-3 overflow-scroll h-full">
			<h2 class="text-xl font-bold text-left">Dashboard</h2>
			<div class="tabs">
				<a
					href={`/admin/dashboard/${applicant ? 'qualifieds' : 'applicants'}`}
					class="tab tab-bordered tab-active"
					class:tab-active={applicant}
					on:click={handleClick}>Applicant</a
				>
				<a
					href={`/admin/dashboard/${!applicant ? 'qualifieds' : 'applicants'}`}
					class="tab tab-bordered"
					class:tab-active={!applicant}
					on:click={handleClick}>Qualified</a
				>
			</div>
			<div class="flex-1 overflow-scroll">
				<slot />
			</div>
			<div>{$message}</div>
		</div>
	</div>
</div>
