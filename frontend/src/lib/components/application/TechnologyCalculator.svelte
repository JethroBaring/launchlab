<script lang="ts">
	export let currentActive: number;
</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 10}>
	<div class="h-0 flex flex-col gap-3">
		<!-- Category 1 -->
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Technology </span>
			</label>
			<div class="form-control">
				<label class="label justify-normal gap-3 cursor-pointer" for="eligibilityAgree">
					<input type="radio" name="eligibility" id="eligibilityAgree" class="radio" value="true" />
					<span class="label-text"
						>Project work is beyond basic research and technology concept has been defined</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Applied research has begun and practical application(s) have been identified</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Preliminary testing of technology components has begun, and technical feasibility has
						been established in a laboratory environment</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Initial testing of integrated product/system has been completed in a laboratory
						environment</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Laboratory scale integrated product/system demonstrates performance in the intended
						application(s)</span
					>
				</label>
			</div>
		</div>
		<!-- Category 2 -->
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Product Development </span>
			</label>
			<div class="form-control">
				<label class="label justify-normal gap-3 cursor-pointer" for="eligibilityAgree">
					<input type="radio" name="eligibility" id="eligibilityAgree" class="radio" value="true" />
					<span class="label-text">Initial product/market fit has been defined</span>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Pilot scale product/system has been tested in the intended application(s)</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Demonstration of a full scale product/system prototype has been completed in the
						intended application(s)</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Actual product/system has been proven to work in its near-final form under a
						representative set of expected conditions and environments</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Product/system is in final form and has been operated under the full range of operating
						conditions and environments</span
					>
				</label>
			</div>
		</div>
		<!-- Category 3 -->
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Product Definition/Design </span>
			</label>
			<div class="form-control">
				<label class="label justify-normal gap-3 cursor-pointer" for="eligibilityAgree">
					<input type="radio" name="eligibility" id="eligibilityAgree" class="radio" value="true" />
					<span class="label-text">One or more initial product hypotheses have been defined</span>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Mapping product/system attributes against customer needs has highlighted a clear value
						proposition</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>The product/system has been scaled from laboratory to pilot scale and issues that may
						affect achieving full scale have been identified</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Comprehensive customer value proposition model has been developed, including a detailed
						understanding of product/system design specifications, required certifications, and
						trade-offs</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Product/system final design optimization has been completed, required certifications
						have been obtained, and product/system has incorporated detailed customer and product
						requirements</span
					>
				</label>
			</div>
		</div>
		<!-- Category 4 -->
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Competitive Landscape </span>
			</label>
			<div class="form-control">
				<label class="label justify-normal gap-3 cursor-pointer" for="eligibilityAgree">
					<input type="radio" name="eligibility" id="eligibilityAgree" class="radio" value="true" />
					<span class="label-text"
						>Secondary market research has been performed and basic knowledge of potential
						applications and competitive landscape have been identified</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Primary market research to prove the product/system commercial feasibility has been
						completed and basic understanding of competitive products/systems has been demonstrated</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Comprehensive market research to prove the product/system commercial feasibility has
						been completed and intermediate understanding of competitive products/systems has been
						demonstrated</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Competitive analysis to illustrate unique features and advantages of the product/system
						compared to competitive products/systems has been completed</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Full and complete understanding of the competitive landscape, target application(s),
						competitive products/systems, and market has been achieved</span
					>
				</label>
			</div>
		</div>
		<!-- Category 5 -->
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Team </span>
			</label>
			<div class="form-control">
				<label class="label justify-normal gap-3 cursor-pointer" for="eligibilityAgree">
					<input type="radio" name="eligibility" id="eligibilityAgree" class="radio" value="true" />
					<span class="label-text"
						>Full and complete understanding of the competitive landscape, target application(s),
						competitive products/systems, and market has been achieved</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text">Solely technical or non-technical founder(s) running the company with no outside assistance</span>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Solely technical or non-technical founder(s) running the company with assistance from outside advisors/mentors and/or incubator/accelerator</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Balanced team with technical and business development/commercialization experience running the company with assistance from outside advisors/mentors</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Balanced team with all capabilities onboard (e.g. sales, marketing, customer service, operations, etc.) running the company with assistance from outside advisors/mentors</span
					>
				</label>
			</div>
		</div>
		<!-- Category 6 -->
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Go-To-Market </span>
			</label>
			<div class="form-control">
				<label class="label justify-normal gap-3 cursor-pointer" for="eligibilityAgree">
					<input type="radio" name="eligibility" id="eligibilityAgree" class="radio" value="true" />
					<span class="label-text"
						>Project work is beyond basic research and technology concept has been defined</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Applied research has begun and practical application(s) have been identified</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Preliminary testing of technology components has begun, and technical feasibility has
						been established in a laboratory environment</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Initial testing of integrated product/system has been completed in a laboratory
						environment</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Laboratory scale integrated product/system demonstrates performance in the intended
						application(s)</span
					>
				</label>
			</div>
		</div>
		<!-- Category 7 -->
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Manufacturing/Supply Chain </span>
			</label>
			<div class="form-control">
				<label class="label justify-normal gap-3 cursor-pointer" for="eligibilityAgree">
					<input type="radio" name="eligibility" id="eligibilityAgree" class="radio" value="true" />
					<span class="label-text"
						>Project work is beyond basic research and technology concept has been defined</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Applied research has begun and practical application(s) have been identified</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Preliminary testing of technology components has begun, and technical feasibility has
						been established in a laboratory environment</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Initial testing of integrated product/system has been completed in a laboratory
						environment</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="eligibility"
						id="eligibilityDisagree"
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Laboratory scale integrated product/system demonstrates performance in the intended
						application(s)</span
					>
				</label>
			</div>
		</div>
	</div>
</div>
