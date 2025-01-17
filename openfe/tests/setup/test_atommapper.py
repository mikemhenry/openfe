import pytest

from openfe.setup.ligandatommapper import LigandAtomMapper


class TestAtomMapper:
    def test_abstract_error(self, simple_mapping):
        # suggest_mappings should fail with NotImplementedError if the user
        # tries to directly user the abstract class
        mol1 = simple_mapping.mol1
        mol2 = simple_mapping.mol2
        mapper = LigandAtomMapper()
        match_re = "'LigandAtomMapper'.*abstract.*_mappings_generator"
        with pytest.raises(NotImplementedError, match=match_re):
            list(mapper.suggest_mappings(mol1, mol2))

    def test_concrete_mapper(self, simple_mapping, other_mapping):
        # a correctly implemented concrete atom mapping should return the
        # mappings generated by the _mappings_generator
        mol1 = simple_mapping.mol1
        mol2 = simple_mapping.mol2

        class ConcreteLigandAtomMapper(LigandAtomMapper):
            def __init__(self, mappings):
                self.mappings = mappings

            def _mappings_generator(self, mol1, mol2):
                for mapping in self.mappings:
                    yield mapping.mol1_to_mol2

        mapper = ConcreteLigandAtomMapper([simple_mapping, other_mapping])
        results = list(mapper.suggest_mappings(mol1, mol2))
        assert len(results) == 2
        assert results == [simple_mapping, other_mapping]
