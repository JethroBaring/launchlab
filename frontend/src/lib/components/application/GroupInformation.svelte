<script lang="ts">
	import { groupInformation } from '$lib/constants';
	export let currentActive: number
</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 2}>
	<div class="h-0">
		{#each groupInformation as field}
			<div class="form-control">
				<label class="label" for={field.name}>
					<span class="label-text">{field.label}</span>
				</label>
				<input
					type="text"
					placeholder={field.placeholder}
					class="input input-bordered"
					id={field.name}
					name={field.name}
				/>
			</div>
		{/each}
	</div>
</div>
