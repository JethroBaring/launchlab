<script lang="ts">
	export let dataPrivacy: boolean, toggleDataPrivacy: Function;
	export let currentActive: number
</script>

<div class="flex-1 overflow-scroll px-6" class:hidden={currentActive !== 0}>
	<div class="h-0">
		<p class="text-lg">
			By accomplishing this form, the following personal information will be collected including,
			startup team members' names, personal email address, mobile phone number and other relevant
			information. The personal information you will provide in this form will be used within
			LaunchLab Program, DASIG consortium committee and will not be shared with any outside parties
			unless you have prior written consent. Development and Acceleration Support for Innovation
			Growth (DASIG) respects your rights as a data subject under the Data Privacy Act.
			<br /><br />
			If you have further questions and concerns regarding the processing of your personal information,
			you are welcome to contact our project lead, Engr. Jurydel Rama, at jurydel.rama@cit.edu.
			<br /><br />
			In compliance with the Data Privacy Act (DPA) of 2012, also known as the Republic Act of 10173
			(RA 10173), I agree and authorize the Development and Acceleration Support for Innovation Growth
			(DASIG) consortium members to use the personal information for the purpose of LaunchLab programs
			and initiatives. I also acknowledge and warrant that I have acquired the consent from all parties
			relevant to this consent and hold free and harmless and indemnify Development and Acceleration
			Support for Innovation Growth (DASIG) from any complaint, suit, or damages which any party may
			file or claim in relation to my consent.
		</p>
		<div class="form-control w-20">
			<label class="label cursor-pointer" for="dataPrivacyAgree">
				<input
					type="radio"
					name="dataPrivacy"
					id="dataPrivacyAgree"
					class="radio"
					on:click={() => toggleDataPrivacy()}
					checked={dataPrivacy === true}
					value="true"
				/>
				<span class="label-text">Agree</span>
			</label>
		</div>
		<div class="form-control w-24">
			<label class="label cursor-pointer" for="dataPrivacyDisagree">
				<input
					type="radio"
					name="dataPrivacy"
					id="dataPrivacyDisagree"
					class="radio"
					on:click={() => toggleDataPrivacy()}
					checked={dataPrivacy === false}
					value="false"
				/>
				<span class="label-text">Disagree</span>
			</label>
		</div>
	</div>
</div>
