
We began by creating a dataset using TIM proteins collected from multiple organisms. For each protein, we retrieved the corresponding cDNA sequences and structural data. Every residue in the structures was then converted into its torsion angles (ϕ, ψ, and ω).

To complement this, we incorporated codon usage information from **Kazusa** and **CodonDB**.

As a result, our final dataset contains, for each organism and its TIM protein:

* The codon sequence and corresponding amino acid (from cDNA and structure),
* The residue’s torsion angles, and
* The codon’s relative frequency based on codon usage tables.




# 🔬 Research Questions to Explore with Codon–Structure Dataset

## 1. **Codon vs Amino Acid Information Content**

1. Do codons encode structural information that amino acid sequences alone cannot capture?
2. Are codons predictive of torsion angles (ϕ, ψ, ω) beyond amino acid identity?
3. Are synonymous codons associated with different local backbone conformations?
4. Do codons influence local flexibility or rigidity more than amino acids?
5. Are codons enriched in specific structural motifs (loops, helices, β-strands, hinges)?
6. Are certain codons preferentially found near active or binding sites?

---

## 2. **Codon Usage Bias**

7. Does codon usage bias vary across organisms for TIM proteins, and how does it relate to structure?
8. Do rare codons occur disproportionately in conserved structural regions?
9. Are rare codons enriched at catalytic residues or functional motifs?
10. Is codon usage bias correlated with torsion angle distributions?
11. Do organisms with stronger codon bias show distinct structural adaptations in TIM proteins?
12. Does codon bias affect conservation of structural motifs across orthologous proteins?

---

## 3. **Translational Kinetics & Co-Translational Folding**

13. Are slow (rare) codons positioned to induce ribosome pausing at folding checkpoints?
14. Do slow codons align with secondary structure boundaries (helix starts, strand edges)?
15. Do rare codons cluster near domain boundaries to facilitate co-translational folding?
16. Do synonymous substitutions shift ribosome stalling points that alter folding?
17. Are ribosome pause sites conserved across organisms, and are they codon-driven?
18. Can codon-driven translation speed explain misfolding vs proper folding?

---

## 4. **Codon Context Effects**

19. Does the identity of neighboring codons (codon context) affect torsion angles?
20. Are codon *pairs* predictive of backbone conformations?
21. Do codon triplets (sliding window context) correlate with secondary structures?
22. Are certain codon contexts enriched in helices vs sheets?
23. Does codon context influence long-range interactions (domain-domain packing)?
24. Do codon neighborhoods explain variability in synonymous codon effects?

---

## 5. **Structure Prediction Framework**

25. Can codon-level representations improve torsion angle prediction compared to amino acids?
26. Do codon-based ML models outperform amino acid–based models in predicting local structures?
27. Can codon-based models capture organism-specific structural biases?
28. Is there a universal codon–structure relationship, or does it vary by organism?
29. Should structure prediction frameworks shift from amino acid–centric to codon–centric representations?
30. Can codon information improve secondary/tertiary structure prediction pipelines?

---

## 6. **Evolutionary and Comparative Aspects**

31. Are synonymous codon substitutions tolerated differently in rigid vs flexible regions?
32. Do codons evolve under stronger constraints at conserved structural motifs?
33. Do codon choices correlate with residue evolutionary rates (dN/dS)?
34. Are codon preferences conserved in evolutionarily distant organisms with TIM proteins?
35. Is codon usage divergence linked to structural divergence across species?
36. Do functionally critical residues exhibit stricter codon usage conservation than neutral ones?

---

## 7. **Integrative Biological Questions**

37. Do codons influence protein misfolding or aggregation propensity?
38. Are codon usage patterns linked to protein stability (thermodynamic stability, folding free energy)?
39. Do codons regulate expression–folding trade-offs (expression speed vs folding accuracy)?
40. Can codon bias fine-tune protein dynamics (flexibility, conformational changes)?
41. Is there a relationship between codon-driven folding and post-translational modifications?
42. Do codons affect structural robustness under stress (heat shock, mutations)?




