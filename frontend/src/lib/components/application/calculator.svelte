<script lang="ts">
	import { technologyReadinessLevel } from '$lib/constants';
	import TechnologyAssessment from '../assessment/TechnologyAssessment.svelte';

	let tech: number = 1,
		dev: number = 1,
		def: number = 1,
		comp: number = 1,
		team: number = 1,
		market: number = 1,
		chain: number = 1;
	let tech1 = 'yes',
		tech2 = 'no',
		tech3 = 'no',
		tech4 = 'no',
		tech5 = 'no';
	let dev1 = 'yes',
		dev2 = 'no',
		dev3 = 'no',
		dev4 = 'no',
		dev5 = 'no';
	let def1 = 'yes',
		def2 = 'no',
		def3 = 'no',
		def4 = 'no',
		def5 = 'no';
	let comp1 = 'yes',
		comp2 = 'no',
		comp3 = 'no',
		comp4 = 'no',
		comp5 = 'no';
	let team1 = 'yes',
		team2 = 'no',
		team3 = 'no',
		team4 = 'no',
		team5 = 'no';
	let market1 = 'yes',
		market2 = 'no',
		market3 = 'no',
		market4 = 'no',
		market5 = 'no';
	let chain1 = 'yes',
		chain2 = 'no',
		chain3 = 'no',
		chain4 = 'no',
		chain5 = 'no';
	let tlevel1 = 'no',
		tlevel2 = 'no',
		tlevel3 = 'no',
		tlevel4 = 'no',
		tlevel5 = 'no',
		tlevel6 = 'no',
		tlevel7 = 'no',
		tlevel8 = 'no',
		tlevel9 = 'no';
	let clevel1 = 'no',
		clevel2 = 'no',
		clevel3 = 'no',
		clevel4 = 'no',
		clevel5 = 'no',
		clevel6 = 'no',
		clevel7 = 'no',
		clevel8 = 'no',
		clevel9 = 'no';
	let technologyLevel = 1,
		commercializationLevel = 1;

	const updateLevel = () => {
		technologyLevel = 1
		commercializationLevel = 1
		tlevel1 = 'no'
		tlevel2 = 'no'
		tlevel3 = 'no'
		tlevel4 = 'no'
		tlevel5 = 'no'
		tlevel6 = 'no'
		tlevel7 = 'no'
		tlevel8 = 'no'
		tlevel9 = 'no'
		clevel1 = 'no'
		clevel2 = 'no'
		clevel3 = 'no'
		clevel4 = 'no'
		clevel5 = 'no'
		clevel6 = 'no'
		clevel7 = 'no'
		clevel8 = 'no'
		clevel9 = 'no'

		if (tech1 === 'yes') {
			tlevel1 = 'yes';
		}
		if (tech2 === 'yes') {
			tlevel2 = 'yes';
		}
		if (tech3 === 'yes') {
			tlevel3 = 'yes';
		}
		if (tech4 === 'yes') {
			tlevel4 = 'yes';
		}
		if (tech5 === 'yes') {
			tlevel5 = 'yes';
		}
		if (dev2 === 'yes' && def3 === 'yes') {
			tlevel6 = 'yes';
		}
		if (dev3 === 'yes') {
			tlevel7 = 'yes';
		}
		if (dev4 === 'yes') {
			tlevel8 = 'yes';
		}
		if (dev5 === 'yes') {
			tlevel9 = 'yes';
		}

		if(comp1 === 'yes' && team1 === 'yes') {
			clevel1 = 'yes'
		}
		if(comp2 === 'yes' && team2 === 'yes') {
			clevel2 = 'yes'
		}
		if(dev1 === 'yes' && def1 === 'yes' && comp3 === 'yes' && team2 === 'yes' && market1 === 'yes') {
			clevel3 = 'yes'
		}
		if(def2 === 'yes' && comp4 === 'yes' && team2 === 'yes' && market2 === 'yes' && chain1 === 'yes') {
			clevel4 = 'yes'
		}
		if(def4 === 'yes' && comp5 === 'yes' && team3 === 'yes' && market3 === 'yes' && chain2 === 'yes') {
			clevel5 = 'yes'
		}
		if(def5 === 'yes' && team4 === 'yes' && market4 === 'yes') {
			clevel6 = 'yes'
		}
		if(team4 === 'yes' && chain3 === 'yes') {
			clevel7 = 'yes'
		}
		if(team5 === 'yes' && chain4 === 'yes') {
			clevel8 = 'yes'
		}
		if(team5 === 'yes' && chain5 === 'yes') {
			clevel9 = 'yes'
		}

		if (tlevel9 === 'yes') {
			technologyLevel = 9;
		} else if (tlevel8 === 'yes') {
			technologyLevel = 8;
		} else if (tlevel7 === 'yes') {
			technologyLevel = 7;
		} else if (tlevel6 === 'yes') {
			technologyLevel = 6;
		} else if (tlevel5 === 'yes') {
			technologyLevel = 5;
		} else if (tlevel4 === 'yes') {
			technologyLevel = 4;
		} else if (tlevel3 === 'yes') {
			technologyLevel = 3;
		} else if (tlevel2 === 'yes') {
			technologyLevel = 2;
		} else if (tlevel1 === 'yes') {
			technologyLevel = 1;
		}
		
		if (clevel9 === 'yes') {
			commercializationLevel = 9;
		} else if (clevel8 === 'yes') {
			commercializationLevel = 8;
		} else if (clevel7 === 'yes') {
			commercializationLevel = 7;
		} else if (clevel6 === 'yes') {
			commercializationLevel = 6;
		} else if (clevel5 === 'yes') {
			commercializationLevel = 5;
		} else if (clevel4 === 'yes') {
			commercializationLevel = 4;
		} else if (clevel3 === 'yes') {
			commercializationLevel = 3;
		} else if (clevel2 === 'yes') {
			commercializationLevel = 2;
		} else if (clevel1 === 'yes') {
			commercializationLevel = 1;
		}

		console.log("technology: " + technologyLevel)
		console.log("commercialization: " + commercializationLevel)
		console.log(tech, dev, def, comp, team, market, chain)
	};

	const updateTech = (techNumber: number) => {
		tech1 = techNumber >= 1 ? 'yes' : 'no';
		tech2 = techNumber >= 2 ? 'yes' : 'no';
		tech3 = techNumber >= 3 ? 'yes' : 'no';
		tech4 = techNumber >= 4 ? 'yes' : 'no';
		tech5 = techNumber >= 5 ? 'yes' : 'no';
		console.log(tech1, tech2, tech3, tech4, tech5)
		tech = techNumber;
		updateLevel();
	};

	const updateDev = (devNumber: number) => {
		dev1 = devNumber >= 1 ? 'yes' : 'no';
		dev2 = devNumber >= 2 ? 'yes' : 'no';
		dev3 = devNumber >= 3 ? 'yes' : 'no';
		dev4 = devNumber >= 4 ? 'yes' : 'no';
		dev5 = devNumber >= 5 ? 'yes' : 'no';
		dev = devNumber;
		updateLevel();
	};

	const updateDef = (defNumber: number) => {
		def1 = defNumber >= 1 ? 'yes' : 'no';
		def2 = defNumber >= 2 ? 'yes' : 'no';
		def3 = defNumber >= 3 ? 'yes' : 'no';
		def4 = defNumber >= 4 ? 'yes' : 'no';
		def5 = defNumber >= 5 ? 'yes' : 'no';
		def = defNumber;
		updateLevel();
	};

	const updateComp = (compNumber: number) => {
		comp1 = compNumber >= 1 ? 'yes' : 'no';
		comp2 = compNumber >= 2 ? 'yes' : 'no';
		comp3 = compNumber >= 3 ? 'yes' : 'no';
		comp4 = compNumber >= 4 ? 'yes' : 'no';
		comp5 = compNumber >= 5 ? 'yes' : 'no';
		comp = compNumber;
		updateLevel();
	};

	const updateTeam = (teamNumber: number) => {
		team1 = teamNumber >= 1 ? 'yes' : 'no';
		team2 = teamNumber >= 2 ? 'yes' : 'no';
		team3 = teamNumber >= 3 ? 'yes' : 'no';
		team4 = teamNumber >= 4 ? 'yes' : 'no';
		team5 = teamNumber >= 5 ? 'yes' : 'no';
		team = teamNumber;
		updateLevel();
	};

	const updateMarket = (marketNumber: number) => {
		market1 = marketNumber >= 1 ? 'yes' : 'no';
		market2 = marketNumber >= 2 ? 'yes' : 'no';
		market3 = marketNumber >= 3 ? 'yes' : 'no';
		market4 = marketNumber >= 4 ? 'yes' : 'no';
		market5 = marketNumber >= 5 ? 'yes' : 'no';
		market = marketNumber;
		updateLevel();
	};

	const updateChain = (chainNumber: number) => {
		chain1 = chainNumber >= 1 ? 'yes' : 'no';
		chain2 = chainNumber >= 2 ? 'yes' : 'no';
		chain3 = chainNumber >= 3 ? 'yes' : 'no';
		chain4 = chainNumber >= 4 ? 'yes' : 'no';
		chain5 = chainNumber >= 5 ? 'yes' : 'no';
		chain = chainNumber;
		updateLevel();
	};

	updateLevel();
</script>

<div class="flex-1 overflow-scroll mb-5 px-6">
	<div class="h-0 flex flex-col gap-3">
		<!-- Category 1 -->
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">Technology </span>
			</label>
			<div class="form-control">
				<label class="label justify-normal gap-3 cursor-pointer" for="eligibilityAgree">
					<input
						type="radio"
						name="technology"
						on:click={() => updateTech(1)}
						id="eligibilityAgree"
						class="radio"
						value="true"
						checked
					/>
					<span class="label-text"
						>Project work is beyond basic research and technology concept has been defined</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="technology"
						on:click={() => updateTech(2)}
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
						name="technology"
						on:click={() => updateTech(3)}
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
						name="technology"
						on:click={() => updateTech(4)}
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
						name="technology"
						on:click={() => updateTech(5)}
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
					<input
						type="radio"
						name="development"
						on:click={() => updateDev(1)}
						id="eligibilityAgree"
						class="radio"
						value="true"
						checked
					/>
					<span class="label-text">Initial product/market fit has been defined</span>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="development"
						on:click={() => updateDev(2)}
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
						name="development"
						on:click={() => updateDev(3)}
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
						name="development"
						on:click={() => updateDev(4)}
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
						name="development"
						on:click={() => updateDev(5)}
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
					<input
						type="radio"
						name="definition"
						on:click={() => updateDef(1)}
						id="eligibilityAgree"
						class="radio"
						value="true"
						checked
					/>
					<span class="label-text">One or more initial product hypotheses have been defined</span>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="definition"
						on:click={() => updateDef(2)}
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
						name="definition"
						on:click={() => updateDef(3)}
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
						name="definition"
						on:click={() => updateDef(4)}
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
						name="definition"
						on:click={() => updateDef(5)}
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
					<input
						type="radio"
						name="competition"
						on:click={() => updateComp(1)}
						id="eligibilityAgree"
						class="radio"
						value="true"
						checked
					/>
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
						name="competition"
						on:click={() => updateComp(2)}
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
						name="competition"
						on:click={() => updateComp(3)}
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
						name="competition"
						on:click={() => updateComp(4)}
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
						name="competition"
						on:click={() => updateComp(5)}
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
					<input
						type="radio"
						name="team"
						on:click={() => updateTeam(1)}
						id="eligibilityAgree"
						class="radio"
						value="true"
						checked
					/>
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
						name="team"
						on:click={() => updateTeam(2)}
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Solely technical or non-technical founder(s) running the company with no outside
						assistance</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="team"
						on:click={() => updateTeam(3)}
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Solely technical or non-technical founder(s) running the company with assistance from
						outside advisors/mentors and/or incubator/accelerator</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="team"
						on:click={() => updateTeam(4)}
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Balanced team with technical and business development/commercialization experience
						running the company with assistance from outside advisors/mentors</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="team"
						on:click={() => updateTeam(5)}
						class="radio"
						value="false"
					/>
					<span class="label-text"
						>Balanced team with all capabilities onboard (e.g. sales, marketing, customer service,
						operations, etc.) running the company with assistance from outside advisors/mentors</span
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
					<input
						type="radio"
						name="market"
						on:click={() => updateMarket(1)}
						id="eligibilityAgree"
						class="radio"
						value="true"
						checked
					/>
					<span class="label-text"
						>Project work is beyond basic research and technology concept has been defined</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="market"
						on:click={() => updateMarket(2)}
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
						name="market"
						on:click={() => updateMarket(3)}
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
						name="market"
						on:click={() => updateMarket(4)}
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
						name="market"
						on:click={() => updateMarket(5)}
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
					<input
						type="radio"
						name="chain"
						on:click={() => updateChain(1)}
						id="eligibilityAgree"
						class="radio"
						value="true"
						checked
					/>
					<span class="label-text"
						>Project work is beyond basic research and technology concept has been defined</span
					>
				</label>
			</div>
			<div class="form-control">
				<label class="label cursor-pointer justify-normal gap-3" for="eligibilityDisagree">
					<input
						type="radio"
						name="chain"
						on:click={() => updateChain(2)}
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
						name="chain"
						on:click={() => updateChain(3)}
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
						name="chain"
						on:click={() => updateChain(4)}
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
						name="chain"
						on:click={() => updateChain(5)}
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
