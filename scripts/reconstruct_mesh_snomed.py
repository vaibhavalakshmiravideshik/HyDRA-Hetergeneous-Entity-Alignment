"""Reconstruct the MeSH-SNOMED-15K benchmark from licensed source data.

This script is intentionally a skeleton to support reproducibility without
redistributing SNOMED CT content directly.

What the user must provide:
1. A locally licensed SNOMED CT release from SNOMED International.
2. The corresponding MeSH release / extracted MeSH-side triples.
3. A local mapping source for MeSH<->SNOMED pairs (e.g., a licensed UMLS-based
   extraction workflow consistent with the paper).

Expected future outputs:
- ent_links
- ent_links_uri
- attr_triples_1
- attr_triples_2
- rel_triples_1
- rel_triples_2

This skeleton is included so users and reviewers can see the intended
reconstruction interface and file layout. Fill in the TODO blocks with your
 local licensed data processing code before public release of a full workflow.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def validate_inputs(mesh_dir: Path, snomed_dir: Path, mapping_file: Path) -> None:
    """Validate that required local licensed inputs exist."""
    missing = [p for p in [mesh_dir, snomed_dir, mapping_file] if not p.exists()]
    if missing:
        missing_str = ", ".join(str(p) for p in missing)
        raise FileNotFoundError(f"Missing required input(s): {missing_str}")


def extract_gold_links(mapping_file: Path):
    """TODO: Parse licensed mapping source and yield MeSH/SNOMED gold pairs."""
    raise NotImplementedError(
        "Implement licensed mapping extraction from your local UMLS/SNOMED workflow."
    )


def build_mesh_triples(mesh_dir: Path):
    """TODO: Extract MeSH attribute and relation triples in benchmark format."""
    raise NotImplementedError("Implement MeSH triple extraction.")


def build_snomed_triples(snomed_dir: Path):
    """TODO: Extract SNOMED CT attribute and relation triples in benchmark format."""
    raise NotImplementedError("Implement SNOMED CT triple extraction.")


def write_outputs(output_dir: Path):
    """Create output directory structure for benchmark artifacts."""
    output_dir.mkdir(parents=True, exist_ok=True)
    expected = [
        "ent_links",
        "ent_links_uri",
        "attr_triples_1",
        "attr_triples_2",
        "rel_triples_1",
        "rel_triples_2",
    ]
    print("Expected output files:")
    for name in expected:
        print(f"  - {output_dir / name}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Reconstruct MeSH-SNOMED-15K from local licensed source data."
    )
    parser.add_argument("--mesh-dir", type=Path, required=True, help="Local MeSH input directory")
    parser.add_argument("--snomed-dir", type=Path, required=True, help="Local SNOMED CT input directory")
    parser.add_argument("--mapping-file", type=Path, required=True, help="Local MeSH-SNOMED mapping source")
    parser.add_argument("--output-dir", type=Path, required=True, help="Output benchmark directory")
    args = parser.parse_args()

    validate_inputs(args.mesh_dir, args.snomed_dir, args.mapping_file)
    write_outputs(args.output_dir)

    print("\nNext steps:")
    print("1. Implement extract_gold_links().")
    print("2. Implement build_mesh_triples().")
    print("3. Implement build_snomed_triples().")
    print("4. Write benchmark TSV files into --output-dir.")


if __name__ == "__main__":
    main()
