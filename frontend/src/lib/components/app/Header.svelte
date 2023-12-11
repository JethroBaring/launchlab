<script lang="ts">
	import { onMount } from 'svelte';

	let isBlurred = false;

	onMount(() => {
		// Listen for the scroll event
		window.addEventListener('scroll', handleScroll);

		// Cleanup the event listener when the component is destroyed
		return () => {
			window.removeEventListener('scroll', handleScroll);
		};
	});

	function handleScroll() {
		// Check the scroll position
		const scrollY = window.scrollY;

		// Set the 'isBlurred' variable based on the scroll position
		isBlurred = scrollY > 100;
	}
</script>

<header
	class="w-screen flex justify-center fixed left-1/2 -translate-x-1/2 top-0"
	class:bg-slate-50={isBlurred}
>
	<nav class="w-4/5 navbar px-0">
		<div class="flex-1 flex gap-2 cursor-pointer">
			<img src="launchlab_logo.png" alt="citeams_logo" class="w-8" />
			<a href="/" class="cursor-pointer font-black normal-case text-2xl">ChumCheck</a>
		</div>
		<div class="flex-none font-semibold">
			<ul class="flex gap-10 text-sm cursor-pointer items-center">
				<li class="active:scale-95">
					<a href="#hero">Home</a>
				</li>
				<li class="active:scale-95">
					<a href="#howitwork">How it Work</a>
				</li>
				<li class="active:scale-95">
					<a href="#aboutus">About Us</a>
				</li>
				<li>
					<a href="/login">
						<button
						class="btn btn-primary btn-custom border-none normal-case text-white bg-flutter-blue shadow-lg shadow-flutter-blue/50"
					>
						Login
					</button></a>
				</li>
			</ul>
		</div>
	</nav>
</header>
