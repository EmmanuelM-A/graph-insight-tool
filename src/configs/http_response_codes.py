"""
HTTP_RESPONSE_CODES: A comprehensive dictionary mapping descriptive constant names to their
integer HTTP response status codes.Each constant is mapped to its official integer HTTP status code, along with an
inline comment explaining its purpose.

The codes are categorized as per HTTP/1.1 and subsequent RFCs:
- 1xx: Informational - Request received, continuing process.
- 2xx: Successful - The action was successfully received, understood, and accepted.
- 3xx: Redirection - Further action needs to be taken to complete the request.
- 4xx: Client Error - The request contains bad syntax or cannot be fulfilled.
- 5xx: Server Error - The server failed to fulfill an apparently valid request.
"""

# 1xx Informational Responses
# Indicates that the request was received and understood. It is issued to inform the client of
# provisional progress in completing the request or that it can continue with its request.
HTTP_CONTINUE = 100  # The server has received the request headers and the client should proceed to send the request body.
HTTP_SWITCHING_PROTOCOLS = 101  # The requester has asked the server to switch protocols and the server has agreed to do so.
HTTP_PROCESSING = 102  # WebDAV: The server has received and is processing the request, but no response is available yet.
HTTP_EARLY_HINTS = 103  # Used to return some response headers before final HTTP response.

# 2xx Successful Responses
# Indicates that the client's request was successfully received, understood, and accepted.
HTTP_OK = 200  # The request has succeeded.
HTTP_CREATED = 201  # The request has been fulfilled and resulted in a new resource being created.
HTTP_ACCEPTED = 202  # The request has been accepted for processing, but the processing has not been completed.
HTTP_NON_AUTHORITATIVE_INFORMATION = 203  # The request was successful, but the enclosed payload has been modified from that of the origin server.
HTTP_NO_CONTENT = 204  # The server successfully processed the request and is not returning any content.
HTTP_RESET_CONTENT = 205  # The server successfully processed the request, but requires the user agent to reset the document view.
HTTP_PARTIAL_CONTENT = 206  # The server is delivering only part of the resource due to a range header by the client.
HTTP_MULTI_STATUS = 207  # WebDAV: Multiple status codes are returned in a single response body.
HTTP_ALREADY_REPORTED = 208  # WebDAV: The members of a DAV binding have already been enumerated in a preceding part of the (multi-status) response.
HTTP_IM_USED = 226  # The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.

# 3xx Redirection Messages
# Indicates that further action needs to be taken by the user agent in order to fulfill the request.
HTTP_MULTIPLE_CHOICES = 300  # Indicates multiple options for the resource from which the client may choose.
HTTP_MOVED_PERMANENTLY = 301  # The requested resource has been assigned a new permanent URI.
HTTP_FOUND = 302  # The requested resource resides temporarily under a different URI.
HTTP_SEE_OTHER = 303  # The response to the request can be found under another URI using a GET method.
HTTP_NOT_MODIFIED = 304  # Indicates that the resource has not been modified since the version specified by the request headers.
HTTP_USE_PROXY = 305  # Deprecated: The requested resource must be accessed through the proxy given by the Location field.
HTTP_SWITCH_PROXY = 306  # No longer used: Intended to mean "Subsequent requests should use the specified proxy."
HTTP_TEMPORARY_REDIRECT = 307  # The request should be repeated with another URI; however, future requests should still use the original URI.
HTTP_PERMANENT_REDIRECT = 308  # The request and all future requests should be repeated using another URI.

# 4xx Client Error Responses
# Indicates that the client seems to have erred.
HTTP_BAD_REQUEST = 400  # The server cannot or will not process the request due to an apparent client error.
HTTP_UNAUTHORIZED = 401  # Authentication is required and has failed or has not yet been provided.
HTTP_PAYMENT_REQUIRED = 402  # Reserved for future use. The original intention was that it might be used as part of some form of digital cash or micropayment scheme.
HTTP_FORBIDDEN = 403  # The server understood the request but refuses to authorize it.
HTTP_NOT_FOUND = 404  # The server can not find the requested resource.
HTTP_METHOD_NOT_ALLOWED = 405  # The request method is known by the server but has been disabled and cannot be used.
HTTP_NOT_ACCEPTABLE = 406  # The server cannot produce a response matching the list of acceptable values defined in the request's proactive negotiation headers.
HTTP_PROXY_AUTHENTICATION_REQUIRED = 407  # Authentication is required with the proxy.
HTTP_REQUEST_TIMEOUT = 408  # The server timed out waiting for the request.
HTTP_CONFLICT = 409  # Indicates that the request could not be processed because of conflict in the current state of the resource.
HTTP_GONE = 410  # The requested resource is no longer available at the server and no forwarding address is known.
HTTP_LENGTH_REQUIRED = 411  # The server refuses to accept the request without a defined Content-Length.
HTTP_PRECONDITION_FAILED = 412  # One or more conditions given in the request header fields evaluated to false when tested on the server.
HTTP_PAYLOAD_TOO_LARGE = 413  # The request entity is larger than limits defined by server.
HTTP_URI_TOO_LONG = 414  # The URI provided was too long for the server to process.
HTTP_UNSUPPORTED_MEDIA_TYPE = 415  # The entity's media type is not supported by the server or resource.
HTTP_RANGE_NOT_SATISFIABLE = 416  # The client has asked for a portion of the file, but the server cannot supply that portion.
HTTP_EXPECTATION_FAILED = 417  # The expectation given in the Expect request-header field could not be met by at least one of the inbound servers.
HTTP_IM_A_TEAPOT = 418  # RFC 2324: I'm a teapot. This code was defined in 1998 as one of the traditional IETF April Fools' jokes.
HTTP_MISDIRECTED_REQUEST = 421  # The request was directed at a server that is not able to produce a response.
HTTP_UNPROCESSABLE_CONTENT = 422  # WebDAV: The request was well-formed but was unable to be followed due to semantic errors.
HTTP_LOCKED = 423  # WebDAV: The resource that is being accessed is locked.
HTTP_FAILED_DEPENDENCY = 424  # WebDAV: The method could not be performed on the resource because the requested action depended on another action that failed.
HTTP_TOO_EARLY = 425  # RFC 8470: Indicates that the server is unwilling to risk processing a request that might be replayed.
HTTP_UPGRADE_REQUIRED = 426  # The client should switch to a different protocol.
HTTP_PRECONDITION_REQUIRED = 428  # RFC 6585: The origin server requires the request to be conditional.
HTTP_TOO_MANY_REQUESTS = 429  # RFC 6585: The user has sent too many requests in a given amount of time.
HTTP_REQUEST_HEADER_FIELDS_TOO_LARGE = 431  # RFC 6585: The server is unwilling to process the request because its header fields are too large.
HTTP_UNAVAILABLE_FOR_LEGAL_REASONS = 451  # RFC 7725: A server operator has received a legal demand to deny access to a resource or to a set of resources that includes the requested resource.

# 5xx Server Error Responses
# Indicates that the server failed to fulfill an apparently valid request.
HTTP_INTERNAL_SERVER_ERROR = 500  # A generic error message, given when an unexpected condition was encountered and no more specific message is suitable.
HTTP_NOT_IMPLEMENTED = 501  # The server does not support the functionality required to fulfill the request.
HTTP_BAD_GATEWAY = 502  # The server, while acting as a gateway or proxy, received an invalid response from an upstream server.
HTTP_SERVICE_UNAVAILABLE = 503  # The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay.
HTTP_GATEWAY_TIMEOUT = 504  # The server, while acting as a gateway or proxy, did not receive a timely response from an upstream server.
HTTP_HTTP_VERSION_NOT_SUPPORTED = 505  # The server does not support the HTTP protocol version used in the request.
HTTP_VARIANT_ALSO_NEGOTIATES = 506  # Indicates that the server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.
HTTP_INSUFFICIENT_STORAGE = 507  # WebDAV: The server is unable to store the representation needed to complete the request.
HTTP_LOOP_DETECTED = 508  # WebDAV: The server detected an infinite loop while processing the request.
HTTP_NOT_EXTENDED = 510  # Further extensions to the request are required for the server to fulfill it.
HTTP_NETWORK_AUTHENTICATION_REQUIRED = 511  # RFC 6585: The client needs to authenticate to gain network access.
