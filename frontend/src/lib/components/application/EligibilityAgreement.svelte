<script lang="ts">
	export let toggleEligibility: Function
	export let eligibility: boolean
	export let currentActive: number;
</script>

<div class="flex-1 overflow-scroll mb-2 px-6" class:hidden={currentActive !== 3}>
	<div class="h-0">
		<p class="text-base">
			I confirm that I have read, understood, and agree to comply with the eligibility criteria and
			rules of the competition. Additionally, I will review the eligibility requirements and
			agreement.
		</p>
		<div class="form-control w-20">
			<label class="label cursor-pointer" for="eligibilityAgree">
				<input
					type="radio"
					name="eligibility"
					id="eligibilityAgree"
					class="radio"
					checked={eligibility === true}
					on:click={() => toggleEligibility()}
					value="true"
				/>
				<span class="label-text">Agree</span>
			</label>
		</div>
		<div class="form-control w-24">
			<label class="label cursor-pointer" for="eligibilityDisagree">
				<input
					type="radio"
					name="eligibility"
					id="eligibilityDisagree"
					class="radio"
					checked={eligibility === false}
					on:click={() => toggleEligibility()}
					value="false"
				/>
				<span class="label-text">Disagree</span>
			</label>
		</div>
	</div>
</div>
