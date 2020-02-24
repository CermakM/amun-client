# coding: utf-8

"""
    Amun API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.6.0-dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amun.swagger_client.configuration import Configuration


class InspectionSpecificationBuildRequests(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cpu': 'str',
        'hardware': 'InspectionSpecificationBuildRequestsHardware',
        'memory': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'hardware': 'hardware',
        'memory': 'memory'
    }

    def __init__(self, cpu=None, hardware=None, memory=None, local_vars_configuration=None):  # noqa: E501
        """InspectionSpecificationBuildRequests - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu = None
        self._hardware = None
        self._memory = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if hardware is not None:
            self.hardware = hardware
        if memory is not None:
            self.memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this InspectionSpecificationBuildRequests.  # noqa: E501

        CPU cores requested at build time.  # noqa: E501

        :return: The cpu of this InspectionSpecificationBuildRequests.  # noqa: E501
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this InspectionSpecificationBuildRequests.

        CPU cores requested at build time.  # noqa: E501

        :param cpu: The cpu of this InspectionSpecificationBuildRequests.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cpu is not None and len(cpu) < 1):
            raise ValueError("Invalid value for `cpu`, length must be greater than or equal to `1`")  # noqa: E501

        self._cpu = cpu

    @property
    def hardware(self):
        """Gets the hardware of this InspectionSpecificationBuildRequests.  # noqa: E501


        :return: The hardware of this InspectionSpecificationBuildRequests.  # noqa: E501
        :rtype: InspectionSpecificationBuildRequestsHardware
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this InspectionSpecificationBuildRequests.


        :param hardware: The hardware of this InspectionSpecificationBuildRequests.  # noqa: E501
        :type: InspectionSpecificationBuildRequestsHardware
        """

        self._hardware = hardware

    @property
    def memory(self):
        """Gets the memory of this InspectionSpecificationBuildRequests.  # noqa: E501

        CPU Memory requested at build time.  # noqa: E501

        :return: The memory of this InspectionSpecificationBuildRequests.  # noqa: E501
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this InspectionSpecificationBuildRequests.

        CPU Memory requested at build time.  # noqa: E501

        :param memory: The memory of this InspectionSpecificationBuildRequests.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                memory is not None and len(memory) < 1):
            raise ValueError("Invalid value for `memory`, length must be greater than or equal to `1`")  # noqa: E501

        self._memory = memory

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InspectionSpecificationBuildRequests):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InspectionSpecificationBuildRequests):
            return True

        return self.to_dict() != other.to_dict()
