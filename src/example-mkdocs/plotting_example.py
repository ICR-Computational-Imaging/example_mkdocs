""" Example python file showing different levels of docstring incorporation """

import argparse  # Useful library for managing terminal command arguments.
from collections.abc import Sequence
from math import ceil, isfinite

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from numpy.typing import NDArray


def calculate_sample_count(frequency: float, duration: float) -> int:
    """Calculate the sample count for at least 30 samples per cycle.

    Args:
        frequency: The sinusoidal frequency in Hz. Its magnitude is used.
        duration: The positive time span in seconds.

    Returns:
        The number of points for an endpoint-inclusive ``np.linspace``.
        One extra point accounts for the endpoint, and at least two points
        are returned for zero frequency or very short time spans.

    Raises:
        ValueError: If frequency or duration is not finite, or duration
            is not positive.
    """
    if not isfinite(frequency):
        raise ValueError("Frequency must be finite.")
    if not isfinite(duration) or duration <= 0:
        raise ValueError("Duration must be finite and greater than zero.")

    return max(2, ceil(30 * abs(frequency) * duration) + 1)


class WavePlotter:
    """ A class for plotting sine waves with a particular frequency

    Attributes:
        frequency: The sinusoidal frequeny in Hz
        amplitude: The amplitude of the sinusoid
    """
    def __init__(self, frequency: float, amplitude: float):
        self.frequency = frequency
        self.amplitude = amplitude

    def plot_sinusoid(self, times: NDArray,
                      axis: Axes | None = None,
                      **kwargs) -> Axes:
        """ Plot the sine wave given the instance variables.

        Args:
            times: The times over which to plot the sinusoid (x-axis).
                   Must have one dimention.
            axis: The matplotlib axes on which to draw the sinusoid.
                  Default is None, in which case a new figure and
                  axis are created.
            kwargs: Additional arguments passed to matplolib.pyplot.plot

        Returns:
            The created axis.  If one is supplied, the instance is returned.

        Raises:
            ValueError: If the times variable does not have a single dimension.
        """

        times = np.array(times)
        if times.ndim != 1:
            raise ValueError("The times value must have a single dimension."
                             f"Input value has {times.ndim} dimensions")

        if axis is None:
            _, axis = plt.subplots(1, 1, figsize=(4, 3))

        angular_frequency = self.frequency * np.pi * 2
        wave = np.sin(angular_frequency * times) * self.amplitude

        axis.plot(times, wave, **kwargs)

        return axis


def plot_sinusoid(times: NDArray, frequency: float = 1.,
                  amplitude: float = 1.):
    """ Fast implementation of plot_sinusoid in the WavePlotter class

    Args:
        times: The times over which to plot the sinusoid (x-axis).
               Must have one dimention.
        frequency: The sinusoidal frequeny in Hz. Default is 1 Hz.
        amplitude: The amplitude of the sinusoid. Default is 1.

    Raises:
        ValueError: If the times variable does not have a single dimension.
    """
    wave_plotter = WavePlotter(frequency=frequency, amplitude=amplitude)
    _ = wave_plotter.plot_sinusoid(times=times,
                                   lw=3.0,
                                   color="r",
                                   linestyle="-")
    plt.tight_layout()
    plt.show()


def _parse_args(arguments: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for final test evaluation."""
    parser = argparse.ArgumentParser(description="Plot a sinusoid curve")
    parser.add_argument("--frequency",
                        type=float,
                        help="The frequency to plot in Hz",
                        required=False,
                        default=1.0)
    parser.add_argument("--amplitude",
                        type=float,
                        help="The amplitude of the sine wave",
                        required=False,
                        default=1.0)
    parser.add_argument("--duration",
                        type=float,
                        help="The duration of the curve in seconds",
                        required=False,
                        default=10.0)
    return parser.parse_args(arguments)


if __name__ == "__main__":
    # Called from command line: python -m example-mkdocs.plotting_example
    args = _parse_args()
    sample_count = calculate_sample_count(args.frequency, args.duration)
    times = np.linspace(0, args.duration, sample_count)
    plot_sinusoid(frequency=args.frequency,
                  amplitude=args.amplitude,
                  times=times)
