<script lang="ts">
	import Icon from '../icons/icon.svelte';
	export let groupName: string,
		leaderName: string,
		leaderEmail: string,
		leaderNumber: any,
		members: any,
		university: any;
	let check = false;

	const handleClick = () => {
		check = !check;
	};
</script>

<div class="collapse">
	<input type="checkbox" checked={check} on:click={handleClick} />
	<div class="collapse-title text-xl font-semibold">
		<div class="flex gap-3 items-center">
			<p>Group Information</p>
			<Icon
				data1={check ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
				data2={null}
			/>
		</div>
	</div>
	<div class="collapse-content flex flex-col gap-3">
		<div class="flex-1">
			<div class="form-control w-96">
				<label class="label" for="">
					<span class="label-text">Group Name</span>
				</label>
				<input
					type="email"
					placeholder="email"
					class="input input-bordered btn-custom"
					name="email"
					required
					value={groupName}
					readonly
				/>
			</div>
		</div>
		<div class="flex gap-10">
			<div class="flex-1">
				<div class="form-control w-96">
					<label class="label" for="">
						<span class="label-text">Leader Name</span>
					</label>
					<input
						type="email"
						placeholder="email"
						class="input input-bordered btn-custom"
						name="email"
						required
						value={leaderName}
						readonly
					/>
				</div>
			</div>
			<div class="flex-1">
				<div class="form-control w-96">
					<label class="label" for="">
						<span class="label-text">Leader Email</span>
					</label>
					<input
						type="email"
						placeholder="email"
						class="input input-bordered btn-custom"
						name="email"
						required
						value={leaderEmail}
						readonly
					/>
				</div>
			</div>
			<div class="flex-1">
				<div class="form-control w-96">
					<label class="label" for="">
						<span class="label-text">Leader Number</span>
					</label>
					<input
						type="email"
						placeholder="email"
						class="input input-bordered btn-custom"
						name="email"
						required
						value={leaderNumber}
						readonly
					/>
				</div>
			</div>
		</div>
		{#each members as member, i}
			{#if member.email !== null && member.email !== undefined}
				<div>
					<div class="form-control w-96">
						<label class="label" for="">
							<span class="label-text">Member {i + 2} Email</span>
						</label>
						<input
							type="email"
							placeholder="email"
							class="input input-bordered btn-custom"
							name="email"
							required
							value={member.email}
							readonly
						/>
					</div>
				</div>
			{/if}
		{/each}
		{#if university}
			<div>
				<div class="form-control w-96">
					<label class="label" for="">
						<span class="label-text">University Name</span>
					</label>
					<input
						type="email"
						placeholder="email"
						class="input input-bordered btn-custom"
						name="email"
						required
						value={university}
						readonly
					/>
				</div>
			</div>
		{/if}
	</div>
</div>
