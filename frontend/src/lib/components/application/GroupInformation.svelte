<script lang="ts">
	import { groupInformation } from '$lib/constants';
	export let currentActive: number;

	let count = 0;
	const x = [
		{
			label: 'Team Member 2 (Last Name, First Name)',
			name: 'member_2_email',
			placeholder: 'team member 2',
			required: false
		},
		{
			label: 'Team Member 3 (Last Name, First Name)',
			name: 'member_3_email',
			placeholder: 'team member 3',
			required: false
		},
		{
			label: 'Team Member 4 (Last Name, First Name)',
			name: 'member_4_email',
			placeholder: 'team member 4',
			required: false
		},
		{
			label: 'Team Member 5 (Last Name, First Name)',
			name: 'member_5_email',
			placeholder: 'team member 5',
			required: false
		}
	];

	const handleClick = (n: number) => {
		count += n;
	};
</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 2}>
	<div class="h-0 flex flex-col gap-3">
		{#each groupInformation as field}
			<div class="form-control">
				<label class="label" for={field.name}>
					<span class="label-text text-base">{field.label}</span>
				</label>
				<input
					type="text"
					placeholder={field.placeholder}
					class="input input-bordered btn-custom"
					id={field.name}
					name={field.name}
				/>
			</div>
		{/each}
		{#each x as item, index}
			{#if index < count}
				<div class="form-control">
					<label class="label" for={item.name}>
						<span class="label-text text-base">{item.label}</span>
					</label>
					<input
						type="text"
						placeholder={item.placeholder}
						class="input input-bordered btn-custom"
						id={item.name}
						name={item.name}
					/>
				</div>
			{/if}
		{/each}
		<div class="w-full flex justify-end gap-3">
			<button on:click|preventDefault={() => handleClick(-1)}>Remove member</button>
			<button on:click|preventDefault={() => handleClick(1)}>Add member</button>
		</div>
	</div>
</div>
