# File: threatq_consts.py
#
# ThreatQuotient Proprietary and Confidential
# Copyright (c) 2016-2025 ThreatQuotient, Inc.
#
# NOTICE: All information contained herein, is, and remains the property of ThreatQuotient, Inc.
# The intellectual and technical concepts contained herein are proprietary to ThreatQuotient, Inc.
# and its suppliers and may be covered by U.S. and Foreign Patents, patents in process, and are
# protected by trade secret or copyright law.
#
# Dissemination of this information or reproduction of this material is strictly forbidden unless prior
# written permission is obtained from ThreatQuotient, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.


THREATQ_NO_DATA = "ThreatQ found no results"
THREATQ_SUCCESS_CONNECTIVITY_TEST = "Successfully connected to ThreatQ"
THREATQ_SUCCESS_UPLOAD_TASK = "Successfully uploaded task to ThreatQ"

THREATQ_TASK_STATUS_MAP = {"To Do": 1, "In Progress": 2, "Review": 3, "Done": 4}
THREATQ_INVESTIGATION_PRIORITY_MAP = {"Normal": 1, "Escalated": 2}
THREATQ_INVESTIGATION_VISIBILITY_MAP = {"Private": 0, "Shared": 1}

# Constants relating to 'get_error_message_from_exception'
ERROR_MESSAGE_UNAVAILABLE = "Error message unavailable. Please check the asset configuration and|or action parameters."

# Constants relating to error messages
THREATQ_ERROR_CONNECTIVITY_TEST = "Failed to connect to ThreatQ. {error}"
THREATQ_ERROR_QUERY_OBJECT_DETAILS = "Error occurred while querying for object details. {error}"
THREATQ_ERROR_GET_RELATED_OBJECTS = "Error occurred while fetching related objects. {error}"
THREATQ_ERROR_SET_DATA_RESPONSE = "Error occurred while adding data and summary to the action result. {error}"
THREATQ_ERROR_PARSE_INDICATOR_LIST = "Error occurred while parsing the 'indicator_list' action parameter. {error}"
THREATQ_ERROR_PARSE_ADVERSARY_LIST = "Error occurred while parsing the 'adversary_list' action parameter. {error}"
THREATQ_ERROR_PARSE_OBJECT_LIST = "Error occurred while parsing the 'object_list' action parameter. {error}"
THREATQ_ERROR_BULK_UPLOAD = "Error occurred while uploading a list of ThreatObjects. {error}"
THREATQ_ERROR_GET_USERS = "Error occurred while getting users. {error}"
THREATQ_ERROR_UPLOAD_TASK = "Failed to upload task to ThreatQ"
THREATQ_ERROR_RELATE_INDICATOR_TO_TASK = "Error occurred while relating indicator {} to the task"
THREATQ_ERROR_RELATE_INDICATORS_TO_TASK = (
    "Error occurred while relating indicators to the task. No indicator was successfully linked with the task."
)
THREATQ_ERROR_RELATE_CONTAINER_EVENT_TO_TASK = "Error occurred while relating container event to the task. {error}"
THREATQ_ERROR_UPLOAD_EVENT = "Failed to upload event to ThreatQ"
THREATQ_ERROR_UPLOAD_SIGNATURE = "Failed uploading signature to ThreatQ"
THREATQ_ERROR_CREATE_INVESTIGATION = "Failed to create investigation"
THREATQ_ERROR_RELATE_INDICATOR_TO_INVESTIGATION = "Error occurred while linking the indicator {} to the investigation"
THREATQ_ERROR_RELATE_INDICATORS_TO_INVESTIGATION = (
    "Error occurred while linking indicators as nodes to the investigation. No indicator was successfully linked with the investigation."
)
THREATQ_ERROR_RELATE_CONTAINER_EVENT_TO_INVESTIGATION = "Error occurred while adding container event to investigation. {error}"
THREATQ_ERROR_FIND_EVENT = "Error occurred while finding event. {error}"
THREATQ_ERROR_UPLOAD_SPEARPHISH = "Error occurred while uploading spearphish event to ThreatQ. {error}"
THREATQ_ERROR_RELATE_CONTAINER_EVENT_TO_SPEARPHISH = "Error occurred while relating container event to the spearphish event. {error}"
THREATQ_ERROR_FIND_FILE = "Error occurred while searching for the file. {error}"
THREATQ_ERROR_UPLOAD_FILE = "Error occurred while uploading file to ThreatQ. {error}"
THREATQ_ERROR_PARSE_FILE = "Error occurred while parsing file for indicators. {error}"
THREATQ_ERROR_RELATE_CONTAINER_EVENT_TO_FILE = "Error occurred while relating container event to the file. {error}"
THREATQ_ERROR_SET_INDICATOR_STATUS = "Error occurred while setting the status of indicator {}"
THREATQ_ERROR_SET_INDICATORS_STATUS = "Error occurred while setting the status of indicators. No indicator's status was successfully updated."
