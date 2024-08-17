from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Match
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from starlette.types import ASGIApp
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry import trace
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from .info import API_ID

def setting_otlp(app: ASGIApp, endpoint: str = None, log_correlation: bool = True) -> None:
  # Setting OpenTelemetry
  # set the service name to show in traces
  resource = Resource.create(attributes={
    "service.name": API_ID,
    "compose_service": API_ID
  })

  # set the tracer provider
  tracer = TracerProvider(resource=resource)
  trace.set_tracer_provider(tracer)

  if endpoint:
    tracer.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint)))

  if log_correlation:
      LoggingInstrumentor().instrument(set_logging_format=True)

  FastAPIInstrumentor.instrument_app(app, tracer_provider=tracer)
