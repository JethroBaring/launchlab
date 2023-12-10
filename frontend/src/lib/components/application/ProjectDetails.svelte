<script lang="ts">
	export let currentActive: number;
</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 1}>
	<div class="h-0  flex flex-col gap-3">
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Startup Name</span>
			</label>
			<input
				type="text"
				placeholder="project title/startup name"
				class="input input-bordered btn-custom"
				id="projectTitle"
				name="name"
			/>
		</div>
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Upload your capsule proposal (PDF max 10mb)</span>
			</label>
			<input
				type="file"
				class="file-input file-input-bordered w-full btn-custom"
				name="capsule_proposal"
			/>
		</div>
		<div class="form-control">
			<label class="label" for="">
				<span class="label-text text-base"
					>Links to any supporting materials (e.g., website, explainer video)</span
				>
			</label>
			<input
				type="text"
				placeholder="links"
				class="input input-bordered btn-custom"
				id="links"
				name="links"
			/>
		</div>
	</div>
</div>
