from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, Union

from .ref import ref_request_builder

class AccessPackageItemRequestBuilder():
    """
    Builds and executes requests for operations under /identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/incompatibleAccessPackages/{accessPackage-id1}
    """
    def ref(self) -> ref_request_builder.RefRequestBuilder:
        """
        Provides operations to manage the collection of identityGovernance entities.
        """
        return ref_request_builder.RefRequestBuilder(self.request_adapter, self.path_parameters)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise Exception("path_parameters cannot be undefined")
        if not request_adapter:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}/incompatibleAccessPackages/{accessPackage%2Did1}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

