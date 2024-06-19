"use client";
import { Checkbox } from "@/components/ui/checkbox";
import { Employee } from "@/types/user";
import { ColumnDef } from "@tanstack/react-table";
import { CellAction } from "./cell-action";

export const columns: ColumnDef<Employee>[] = [
  {
    id: "select",
    header: ({ table }) => (
      <Checkbox
        checked={table.getIsAllPageRowsSelected()}
        onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
        aria-label="Selectionner tout"
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={(value) => row.toggleSelected(!!value)}
        aria-label="Selectionner une ligne"
      />
    ),
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: "first_name",
    header: "Nom",
  },
  {
    accessorKey: "country",
    header: "Prénoms",
  },
  {
    accessorKey: "email",
    header: "Email",
  },
  {
    accessorKey: "job",
    header: "COMPANY",
  },
  {
    accessorKey: "gender",
    header: "GENDER",
  },
  {
    id: "actions",
    cell: ({ row }) => <CellAction data={row.original} />,
  },
];
