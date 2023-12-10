<script lang="ts">
	import type { ActionData } from './$types';
	export let form: ActionData;
</script>

<svelte:head>
	<title>Login</title>
</svelte:head>

<div class="flex-1 flex-col h-full rounded-inherit flex items-center relative">
	<div class="p-5 flex gap-2 cursor-pointer items-center w-full absolute">
		<img src="launchlab_logo.png" alt="citeams_logo" class="w-8" />
		<a href="/" class="cursor-pointer font-black normal-case text-2xl">ChumCheck</a>
	</div>
	
	<div class="flex-1 flex items-center justify-center">
		<img src="login.png" alt="" class="w-96 h-96" />
	</div>
</div>
<div class="flex-1 flex flex-col gap-5 items-center justify-between h-full">
	<div class="flex-1 flex flex-col w-full p-10 justify-center">
		<h1 class="text-2xl font-semibold mb-5">Login</h1>
		<form action="?/login" method="post">
			<div class="form-control w-3/4">
				<label class="label" for="">
					<span class="label-text">Email</span>
				</label>
				<input
					type="email"
					placeholder="email"
					class="input input-bordered btn-custom"
					name="email"
					required
					value={form?.email ?? ''}
				/>
			</div>
			<div class="form-control w-3/4">
				<label class="label" for="">
					<span class="label-text">Password</span>
				</label>
				<input
					type="password"
					placeholder="password"
					class="input input-bordered btn-custom"
					name="password"
					required
				/>
			</div>
			{#if form?.credentials}
				<p>Invalid credentials</p>
			{/if}
			<button
				class="btn mt-8 btn-primary btn-custom border-none normal-case text-white bg-flutter-blue shadow-lg shadow-flutter-blue/50"
			>
				Login
			</button>
		</form>
	</div>
</div>
