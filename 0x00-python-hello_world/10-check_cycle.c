#include "lists.h"

/**
  * check_cycle - check_cycle
  * @list: list_t
  * Return: int
  */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	int i = 0;

	while (temp)
	{
		if (i != 0 && temp == list)
			return (1);
		temp = temp->next;
		i++;
	}
	return (0);
}
