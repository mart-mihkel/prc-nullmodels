import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    import pandas as pd

    from nullmodels import pr_quantile_hypergeom
    from plotnine import ggplot, aes, geom_line, ggtitle, theme_bw

    return (
        aes,
        geom_line,
        ggplot,
        ggtitle,
        np,
        pd,
        pr_quantile_hypergeom,
        theme_bw,
    )


@app.cell
def _(
    aes,
    geom_line,
    ggplot,
    ggtitle,
    np,
    pd,
    pr_quantile_hypergeom,
    theme_bw,
):
    n = 25
    p_ub, r_ub, th = pr_quantile_hypergeom(n, q=0.9)
    p_lb, r_lb, _ = pr_quantile_hypergeom(n, q=0.1)

    df = pd.DataFrame(
        {
            "Precision": np.concatenate((p_ub, p_lb)),
            "Recall": np.concatenate((r_ub, r_lb)),
            "Threshold": np.tile(th, 2),
        }
    )

    (
        ggplot(df)
        + aes("Recall", "Precision", color="Threshold", group="Threshold")
        + geom_line()
        + ggtitle(
            r"Hypergeom $\bar{q}_{0.9}$ to $q_{0.9}$ per classification threshold"
        )
        + theme_bw()
    ).show()
    return


if __name__ == "__main__":
    app.run()
