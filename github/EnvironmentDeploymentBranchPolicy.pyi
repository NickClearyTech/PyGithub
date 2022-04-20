import github.GithubObject
import github.EnvironmentProtectionRuleReviewer


class EnvironmentDeploymentBranchPolicy(github.GithubObject.CompletableGithubObject):
    @property
    def protected_branches(self) -> bool: ...
    @property
    def custom_branch_policies(self) -> bool: ...


class EnvironmentDeploymentBranchPolicyParams:
    def __init__(self, protected_branches: bool=..., custom_branch_policies: bool=...): ...
    def _asdict(self) -> dict: ...
