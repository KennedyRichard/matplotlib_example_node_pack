
### third-party import

from matplotlib.figure import Figure

def _save_figure(

      figure: Figure,
      fname:'image_filepath'='.',
      *,
      format:'python_literal'=None,
      dpi: 'python_literal' = 'figure',
      metadata: dict = None,
      bbox_inches: 'python_literal'=None,
      pad_inches: 'python_literal' = 0.1,
      face_color: 'python_literal' = 'auto',
      edge_color: 'python_literal' = 'auto',
      backend: 'python_literal' = None,
      **kwargs

    ):

    Figure.savefig(
             figure,
             fname=fname,
             format=format,
             dpi=dpi,
             metadata=metadata,
             bbox_inches=bbox_inches,
             pad_inches=pad_inches,
             face_color=face_color,
             edge_color=edge_color,
             backend=backend,
             **kwargs
           )

main_callable = Figure.savefig
signature_callable = _save_figure
call_format = 'Figure.savefig'
third_party_import_text = 'from matplotlib.figure import Figure'
