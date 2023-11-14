<script lang="ts">
	export let currentActive: number
</script>
<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 1}>
	<div class="h-0">
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text">Project Title/Startup Name</span>
			</label>
			<input
				type="text"
				placeholder="project title/startup name"
				class="input input-bordered"
				id="projectTitle"
				name="starup_name"
			/>
		</div>
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text">Upload your capsule proposal (PDF max 10mb)</span>
			</label>
			<input type="file" class="file-input file-input-bordered w-full" name="capsule_proposal"/>
		</div>
		<div class="form-control">
			<label class="label" for="">
				<span class="label-text"
					>Links to any supporting materials (e.g., website, explainer video)</span
				>
			</label>
			<input type="text" placeholder="links" class="input input-bordered" id="links" name="links" />
		</div>
	</div>
</div>
