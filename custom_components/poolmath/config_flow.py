"""Config flow for Pool Math integration."""

import logging
from typing import Any, Union

import voluptuous as vol

from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    OptionsFlow,
)
from homeassistant.const import CONF_NAME, __version__ as HAVERSION
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_validation as cv

from .const import (
    CONF_USER_ID,
    CONF_POOL_ID,
    CONF_TARGET,
    CONF_TIMEOUT,
    DEFAULT_NAME,
    DEFAULT_TARGET,
    DEFAULT_TIMEOUT,
    DOMAIN,
    INTEGRATION_NAME,
)

LOG = logging.getLogger(__name__)


def _initial_form(flow: Union[ConfigFlow, OptionsFlow]):
    """Return flow form for init/user step id."""

    if isinstance(flow, ConfigFlow):
        step_id = "user"
        user_id = None
        pool_id = None
        name = DEFAULT_NAME
        timeout = DEFAULT_TIMEOUT
        target = DEFAULT_TARGET
    elif isinstance(flow, OptionsFlow):
        step_id = "init"
        user_id = flow.config_entry.options.get(CONF_USER_ID)
        pool_id = flow.config_entry.options.get(CONF_POOL_ID)
        name = flow.config_entry.options.get(CONF_NAME, DEFAULT_NAME)
        timeout = flow.config_entry.options.get(CONF_TIMEOUT, DEFAULT_TIMEOUT)
        target = flow.config_entry.options.get(CONF_TARGET, DEFAULT_TARGET)
    else:
        raise TypeError("Invalid flow type")

    return flow.async_show_form(
        step_id=step_id,  # parameterized to follow guidance on using "user"
        data_schema=vol.Schema(
            {
                vol.Required(CONF_USER_ID, default=user_id): cv.string,
                vol.Required(CONF_POOL_ID, default=pool_id): cv.string,
                vol.Optional(CONF_NAME, default=name): cv.string,
                vol.Optional(CONF_TIMEOUT, default=timeout): cv.positive_int,
                # NOTE: targets are not really implemented, other than tfp
                vol.Optional(
                    CONF_TARGET, default=target
                ): cv.string,  # targets/*.yaml file with min/max targets
                # FIXME: allow specifying EXACTLY which log types to monitor, always create the sensors
                # vol.Optional(CONF_LOG_TYPES, default=None):
            }
        ),
    )


class PoolMathOptionsFlow(OptionsFlow):
    """Handle Pool Math options."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize options flow."""
        if AwesomeVersion(HAVERSION) < "2024.11.99":
            self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage Pool Math options."""
        if user_input is not None:
            return self.async_create_entry(title=INTEGRATION_NAME, data=user_input)

        return _initial_form(self)


class PoolMathFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a Pool Math config flow."""

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            # already configured user_id and pool_id?
            user_id = user_input.get(CONF_USER_ID)
            pool_id = user_input.get(CONF_POOL_ID)
            await self.async_set_unique_id(user_id + "-" + pool_id)
            self._abort_if_unique_id_configured()

            return self.async_create_entry(title=INTEGRATION_NAME, data=user_input)

        return _initial_form(self)

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> PoolMathOptionsFlow:
        """Get the options flow for this handler."""
        return PoolMathOptionsFlow(config_entry)
